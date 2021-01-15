<template>
  <div>
    <golden-layout class="hscreen">
      <gl-col>
        <layout :state="portState" />
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
</style>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

import Layout from "@/components/Layout.vue";

@Component({
  components: {
    Layout,
  },
})
export default class Ports extends Vue {
  portState = {
    name: "Ports",
    stackSubs: [1, 2, 3, 4, 5],
    ssid: 1,
  };
}
</script>
