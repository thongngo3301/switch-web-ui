<template>
  <gl-row>
    <gl-component
      title="compA"
      class="test-component"
      width="30"
      :closable="false"
      :reorderEnabled="false"
      :showPopoutIcon="false"
      :state.sync="mainState"
    >
      <input v-model="mainState.text" />
      <h1>CompA</h1>
      <button @click="addStack">Add</button>
      <p><input v-model="testText" /></p>
    </gl-component>
    <gl-dstack>
      <gl-component
        v-for="stackSub in state.stackSubs"
        :key="stackSub"
        :title="'dynamic' + stackSub"
        @destroy="remStack(stackSub)"
      >
        Dynamic item (id: {{ stackSub }})
        <button @click="remStack(stackSub)">Remove</button>
        <p><input v-model="testText" /></p>
      </gl-component>
    </gl-dstack>
  </gl-row>
</template>

<style>
.lm_controls {
  display: none;
}
</style>

<script lang="ts">
import { Component, Prop } from "vue-property-decorator";
import { glCustomContainer } from "vue-golden-layout";

@Component
export default class Layout extends glCustomContainer {
  @Prop() state!: {
    stackSubs: number[];
    ssid: number;
  };
  mainState: unknown = { text: "Nothing new" };
  testText = "testing text.";
  addStack() {
    this.state.stackSubs.push(++this.state.ssid);
  }
  remStack(id: number) {
    const ndx = this.state.stackSubs.indexOf(id);
    if (~ndx) this.state.stackSubs.splice(ndx, 1);
    else console.assert(false, "Closed dynamic component is in the array");
  }
}
</script>
