<template>
 <v-data-table
      :headers="headers"
      :items="desserts"
      sort-by="id"
      class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
          flat
      >
        <v-toolbar-title>任务列表</v-toolbar-title>
        <v-divider
            class="mx-4"
            inset
            vertical
        ></v-divider>
        <v-spacer></v-spacer>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }" >
      <v-btn
          small
          color="green accent-3"
          @click="show(item)"
      >
        查看报告
      </v-btn>
      <v-btn color="green"  @click="checkReport(item)">查看报告</v-btn>
    </template>

  </v-data-table>
</template>

<script>

export default {
  data: () => ({
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: '任务id',
        align: 'start',
        sortable: false,
        value: 'id',
      },
      {text: '任务描述', value: 'remark'},
      {text: '创建时间', value: 'create_at'},
      {text: 'Actions', value: 'actions'},
    ],

  }),
  watch: {

  },

  created() {
    this.initialize()
  },

  methods: {
    initialize() {
      this.$api.task.get_task().then((res)=>{
        if (res.data.code === 0){
          this.desserts = res.data.data
          this.$toast(res.data.msg)
        } else {
          this.$toast(res.data.msg, 4)
        }
      })
      this.desserts = []
    },

    show(item) {

      const showId = item.id;
      console.log(showId);

    },

  },
}
</script>

<style scoped>

</style>