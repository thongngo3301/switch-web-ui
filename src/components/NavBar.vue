<template>
  <span>
    <v-app-bar
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
              <!-- {{ item.title }} -->
              <v-btn text class="hidden-sm-and-down">{{ item.title }}</v-btn>
            </v-list-item-content>
          </v-list-item>
          <v-divider :key="`divider-${index}`"></v-divider>
        </template>
      </v-list>
    </v-app-bar>
    <v-app-bar app color="brown darken-4" dark>
      <v-app-bar-nav-icon
        class="hidden-md-and-up"
        @click="drawer = !drawer"
      ></v-app-bar-nav-icon>
      <!-- <v-spacer class="hidden-md-and-up"></v-spacer>
      <v-toolbar-title>{{ appTitle }}</v-toolbar-title>
      <v-btn text class="hidden-sm-and-down">Menu</v-btn>
      <v-spacer class="hidden-sm-and-down"></v-spacer>
      <v-btn text class="hidden-sm-and-down">Sign In</v-btn> -->
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
      items: [{ title: "Menu" }, { title: "Sign In" }]
    };
  }
};
</script>

<style scoped></style>
