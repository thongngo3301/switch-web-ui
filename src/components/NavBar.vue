<template>
  <span>
    <!-- <v-app-bar
      app
      v-model="drawer"
      class="brown lighten-2"
      dark
      disable-resize-watcher
    >
      <v-list>
        <template v-for="(item, index) in items">
          <v-list-item :key="index">
            <v-list-item-content>
              {{ item.title }}
            </v-list-item-content>
          </v-list-item>
          <v-divider :key="`divider-${index}`"></v-divider>
        </template>
      </v-list>
    </v-app-bar> -->
    <v-app-bar app color="brown darken-4" dark>
      <!-- <v-app-bar-nav-icon
        class="hidden-md-and-up"
        @click="drawer = !drawer"
      ></v-app-bar-nav-icon> -->
      <v-toolbar-title>{{ appTitle }}</v-toolbar-title>
      <v-spacer class="hidden-md-and-up"></v-spacer>
      <template v-for="(item, index) in items">
        <v-btn :key="index" text class="hidden-sm-and-down" :to="`/${item.title}`">
          {{ item.title }}
        </v-btn>
        <v-divider :key="`divider-${index}`"></v-divider>
      </template>
    </v-app-bar>
  </span>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      appTitle: "Test",
      drawer: false,
      items: [{ title: "comm" }, { title: "ports" }, { title: "acl" },
              { title: "qos" }, { title: "flows" }, { title: "stp" },
              { title: "openflow" }, { title: "bridge" }, { title: "ssl" },
              { title: "controller" }, { title: "manager" }, { title: "openvswitch" }, { title: "ip" }]
    };
  }
};
</script>

<style scoped></style>
