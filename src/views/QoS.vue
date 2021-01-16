<template>
  <div>
    <golden-layout class="hscreen" v-if="this.isReady">
      <gl-col>
        <layout :state="this.qosState" />
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
import { Component, Prop, Vue } from "vue-property-decorator";
import axios from "axios";

import Layout from "@/components/Layout.vue";

@Component({
  components: {
    Layout
  }
})
export default class QoS extends Vue {
  @Prop() qosState!: object;
  @Prop({ default: "http://192.168.1.188:5000" }) readonly server_addr!: string;
  @Prop({ default: "/qos" }) readonly path!: string;
  @Prop() msg!: string;
  @Prop({ default: false }) isReady!: boolean;

  public getQos(): void {
    axios.get(this.server_addr + this.path).then(res => {
      this.msg = res.data;
      console.log(res, this.msg);
      this.qosState = {
        name: "QoS",
        stackSubs: [3, 2, 1],
        ssid: 1
      };
      this.isReady = true;
    });
  }

  mounted() {
    this.getQos();
  }
}
</script>
