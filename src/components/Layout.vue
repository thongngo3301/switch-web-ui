<template>
  <gl-row>
    <gl-component
      :title="state.name"
      class="test-component"
      width="30"
      :closable="false"
      :reorderEnabled="false"
      :state.sync="mainState"
    >
      <input v-model="mainState.text" />
      <h1>CompA</h1>
      <button @click="addStack">Add</button>
      <p><input v-model="testText" /></p>
    </gl-component>
    <gl-stack>
      <gl-component
        v-for="stackSub in state.stackSubs"
        :key="stackSub"
        :closable="false"
        :reorderEnabled="false"
        :title="'dynamic' + stackSub"
      >
        Dynamic item (id: {{ stackSub }})
        <button @click="remStack(stackSub)">Remove</button>
        <p><input v-model="testText" /></p>
      </gl-component>
    </gl-stack>
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
    name: string;
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
