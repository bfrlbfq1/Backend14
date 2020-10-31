<template>
  <v-app>
    <v-snackbar
      v-model="snackbar"
      :timeout="2"
    >
      {{ text_msg }}
    </v-snackbar>
    <!-- 路由出口 -->
  <!-- 路由匹配到的组件将渲染在这里 -->
    <router-view></router-view>
  </v-app>
</template>

<script>
  export default {
    name: 'App',
    components: {
    },
  data: () => ({
    //
  }),
};
</script>