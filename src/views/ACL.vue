<template>
  <div>
    <golden-layout class="hscreen">
      <gl-col>
        <layout :state="aclState" />
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
export default class ACL extends Vue {
  aclState = {
    name: "ACL",
    stackSubs: [9, 8, 7],
    ssid: 1,
  };
}
</script>
