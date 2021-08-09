<template>
  <v-app>
    <v-navigation-drawer app>


      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            测试平台
          </v-list-item-title>
          <v-list-item-subtitle>
            v 1.0
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
          dense
          nav
      >
        <v-list-item
            v-for="item in items"
            :key="item.title"
            @click="switchTab(item.router)"
            link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <!-- -->
    </v-navigation-drawer>

    <v-app-bar app>
      <!-- -->
    </v-app-bar>

    <!-- 根据应用组件来调整你的内容 -->
    <v-main>

      <!-- 给应用提供合适的间距 -->
      <v-container fluid>

        <!-- 如果使用 vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "Layout",
  data() {
    return {
      items: [
        {title: '测试用例', icon: 'mdi-image', router: 'Testcase'},
        {title: '测试任务', icon: 'mdi-view-dashboard', router: 'Task'},
      ],
      right: null,
    }
  },
  methods: {
    switchTab(router) {
      this.$router.push({"name": router})
    }
  }
}
</script>

<style scoped>

</style>