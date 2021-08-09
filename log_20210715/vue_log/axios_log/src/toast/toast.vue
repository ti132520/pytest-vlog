<template>
  <div class="app-toast"
       v-if="isShow"
       :class="{'info': type=== 1,'success': type=== 2,
       'wraning': type=== 3,'danger': type=== 4}">{{ text }}
  </div>
</template>

<script>
export default {
  name: "toast"
}
</script>

<style scoped>
.app-toast {
  position: fixed;
  left: 50%;
  top: 50%;
  background: #ccc;
  padding: 10px;
  border-radius: 5px;
  transform: translate(-50%, -50%);
  color: #fff;
}

.info {
  background: #00aaee;
}

.success {
  background: #00ee6b;
}

.wraning {
  background: #eea300;
}

.danger {
  background: #ee000c;
}
</style>