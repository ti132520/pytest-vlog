<template>
  <div>
    <v-alert
        v-show="false"
        id="alert"
        dense
        type="info"
    >
    </v-alert>
    <v-data-table
        v-model="selected"
        item-key="id"
        show-select
        :headers="headers"
        :items="desserts"
        sort-by="id"
        class="elevation-1"
    >

      <template v-slot:top>
        <v-toolbar
            flat
        >
          <v-toolbar-title>用例列表</v-toolbar-title>
          <v-divider
              class="mx-4"
              inset
              vertical
          ></v-divider>
          <v-spacer></v-spacer>
          <v-dialog
              v-model="dialog"
              max-width="500px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                  color="primary"
                  dark
                  class="mb-2"
                  v-bind="attrs"
                  v-on="on"
              >
                新增用例
              </v-btn>
              <v-btn
                  color="green"
                  dark
                  class="mb-2"
                  @click="executeCase"
              >
                执行用例
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col
                        cols="12"
                        sm="6"
                        md="4"
                    >
                      <v-text-field
                          v-model="editedItem.id"
                          label="id"
                          disabled
                      ></v-text-field>
                    </v-col>
                    <v-col
                        cols="12"
                        sm="6"
                        md="4"
                    >
                      <v-text-field
                          v-model="editedItem.nodeId"
                          label="nodeId"
                      ></v-text-field>
                    </v-col>
                    <v-col
                        cols="12"
                        sm="6"
                        md="4"
                    >
                      <v-text-field
                          v-model="editedItem.remark"
                          label="备注"
                      ></v-text-field>
                    </v-col>

                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    color="blue darken-1"
                    text
                    @click="close"
                >
                  取消
                </v-btn>
                <v-btn
                    color="blue darken-1"
                    text
                    @click="save"
                >
                  保存
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5">要删除这条用例吗?</v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDelete">取消</v-btn>
                <v-btn color="blue darken-1" text @click="deleteItemConfirm">确定</v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon
            small
            class="mr-2"
            @click="editItem(item)"
        >
          mdi-pencil
        </v-icon>
        <v-icon
            small
            @click="deleteItem(item)"
        >
          mdi-delete
        </v-icon>
      </template>
    </v-data-table>
  </div>


</template>

<script>
export default {
  data: () => ({
    selected: [],
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: 'id',
        align: 'start',
        sortable: false,
        value: 'id',
      },
      {text: 'nodeId', value: 'nodeId'},
      {text: '备注', value: 'remark'},
      {text: '时间', value: 'create_at'},
      {text: 'Actions', value: 'actions', sortable: false},
    ],
    desserts: [],
    editedIndex: -1,
    editedItem: {},
    defaultItem: {
      nodeId: '',
      remark: '',
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? '新建用例' : '编辑用例'
    },
  },

  watch: {
    dialog(val) {
      val || this.close()
    },
    dialogDelete(val) {
      val || this.closeDelete()
    },
  },

  created() {
    this.initialize()
  },

  methods: {
    initialize() {
      this.$api.testcase.getTestcase().then((result) => {
        if (result.data.code === 0) {
          this.desserts = result.data.data
        } else {
          this.$toast(result.data.msg, 4)
        }
      }).catch((err) => {
        this.$toast(err, 4)
      })

    },

    editItem(item) {
      this.editedIndex = this.desserts.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem(item) {
      this.editedIndex = this.desserts.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    deleteItemConfirm() {
      this.$api.testcase.deleteTestcase(this.editedItem).then((res) => {
        if (res.data.code === 0) {
          this.$toast(res.data.msg, 2)
          this.desserts.splice(this.editedIndex, 1)
          this.closeDelete()
        }
      }).catch((err) => {
        this.$toast(err, 4)
      })

    },

    close() {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    closeDelete() {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    save() {
      if (this.editedIndex > -1) {
        this.$api.testcase.updateTestcase(this.editedItem).then((res) => {
          if (res.data.code === 0) {
            this.$toast(res.data.msg, 2)
            this.initialize()
          } else {
            this.$toast(res.data.msg, 4)
          }
        }).catch(() => {
          this.initialize()
          // this.$toast(err, 4)
        })

      } else {
        this.$api.testcase.addTestcase(this.editedItem).then((res) => {
          console.log(res);
          if (res.data.code === 0) {
            this.initialize()
            this.$toast(res.data.msg, 2)
          } else {
            this.$toast(res.data.msg, 4)
          }
        }).catch((err) => {
          this.$toast(err, 4)
        })
      }
      this.close()
    },
    // 执行用例
    executeCase() {
      console.log(this.selected);
    }
  },
}
</script>
