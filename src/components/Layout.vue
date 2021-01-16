<template>
  <gl-row>
    <gl-component
      :title="state.name"
      class="test-component"
      width="30"
      :closable="false"
      :reorderEnabled="false"
      :state.sync="state"
    >
      <h1>CompA</h1>
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
}
</script>
