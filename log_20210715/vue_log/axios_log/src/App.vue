<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>

<script>
export default {
  created: function () {
    this.initialize()
  },
  methods: {
    initialize() {
      if (!localStorage.getItem('token')) {
        this.$api.token.get_token().then((res) => {
          if (res.data.code === 0) {
            localStorage.setItem('token', res.data.data.token)
          } else {
            this.$toast(res.data.msg)
          }
        })
      }
    }
  }
}
</script>
