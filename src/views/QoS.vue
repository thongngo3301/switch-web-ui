<template>
  <div>
    <golden-layout class="hscreen">
      <gl-col>
        <layout :state="qosState" />
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
import axios from "axios";

import Layout from "@/components/Layout.vue";

@Component({
  components: {
    Layout,
  },
})
export default class QoS extends Vue {
  qosState = {
    name: "QoS",
    stackSubs: [3, 2, 1],
    ssid: 1,
  };
  mounted() {
    const req = {
      title: "abc"
    };
    axios.post(`http://127.0.0.1:8888/qos`, req, {
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-type': 'application/json'
      }
    })
      .then(res => {
        // this.resp = res
        console.log(res);
      })
  }
}
</script>
