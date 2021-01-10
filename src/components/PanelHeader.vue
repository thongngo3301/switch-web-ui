<template>
  <div>Title: {{ title }}</div>
</template>
<script lang="ts">
import Vue from "vue";
import { Component, Prop } from "vue-property-decorator";

@Component
export default class PanelHeader extends Vue {
  @Prop() public title!: string;
}
</script>
