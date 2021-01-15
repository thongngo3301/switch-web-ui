<template>
  <div>
    <golden-layout class="hscreen" v-model="state" @creation-error="reset">
      <gl-col>
        <layout :state="stackState" />
      </gl-col>
    </golden-layout>
  </div>
</template>

<style>
body {
  overflow: hidden; /* The 'light' theme let a scroll-bar on the right of the main container */
}
.hscreen {
  width: 100vw;
  height: 100vh;
}
.reset {
  position: absolute;
  bottom: 0;
  right: 0;
  float: right;
  z-index: 9000;
}
.reset:hover {
  background-color: red;
}
</style>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

import PanelHeader from "@/components/PanelHeader.vue";
import Layout from "@/components/Layout.vue";

@Component({
  components: {
    PanelHeader,
    Layout
  }
})
export default class Home extends Vue {
  state: unknown = null;
  stackState = {
    name: "Home",
    stackSubs: [1],
    ssid: 1
  };
  reset() {
    delete localStorage.browserGL;
    location.reload();
  }
}
</script>
