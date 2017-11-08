<template>
  <div>
    <h>未完成</h>
    <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
      <el-tab-pane label="所有报名" name="1"></el-tab-pane>
      <el-tab-pane label="审核中" name="2"></el-tab-pane>
      <el-tab-pane label="已通过" name="3"></el-tab-pane>
      <el-tab-pane label="未通过" name="4"></el-tab-pane>
    </el-tabs>
    <el-table
      :data="filteredTable"
      border
      :show-header="true"
      style="width: 100%">
      <el-table-column
        prop="project_name"
        label="项目名称"
        width="180">
      </el-table-column>
      <el-table-column
        prop="contact_info"
        label="联系人"
        >
      </el-table-column>
      <el-table-column
        prop="register_state"
        label="报名状态"
        width="100">
      </el-table-column>
      <el-table-column
        label="报名状态"
        width="100"
        prop="register">
        <template scope="scope">
          <el-button @click="malert(scope.row)" type="text" size="small">查看/修改</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>

</template>

<script>
  export default {
    data () {
      return {
        activeName: '1',
        tableData: [{
          project_name: '足球',
          contact_info: '郭志芃',
          contact_tel: '18813040000',
          register_state: '审核中'
        }, {
          project_name: '足球',
          contact_info: '郭志芃',
          contact_tel: '18813040000',
          register_state: '已通过'
        }, {
          project_name: '足球',
          contact_info: '郭志芃',
          contact_tel: '18813040000',
          register_state: '审核中'
        }, {
          project_name: '篮球',
          contact_info: '郭志芃',
          contact_tel: '18813040000',
          register_state: '未通过'
        }, {
          project_name: '足球',
          contact_name: '郭志芃',
          contact_tel: '18813040000',
          register_state: '已通过'
        }, {
          project_name: '乒乓球',
          contact_info: '郭志芃',
          contact_tel: '18813040000',
          register_state: '审核中'
        }, {
          project_name: '足球',
          contact_info: '郭志芃',
          contact_tel: '18813040000',
          register_state: '未通过'
        }]
      }
    },
    methods: {
      handleClick (row) {
        console.log(this.activeName.toString())
      },
      malert (row) {
        alert(row.project_name)
      }
    },
    computed: {
      filteredTable: function () {
        switch (this.activeName.toString()) {
          case '1':
            console.log(this.activeName)
            return this.tableData
          case '2':
            return this.tableData.filter(function (item) {
              return item.register_state === '审核中'
            })
          case '3':
            return this.tableData.filter(function (item) {
              return item.register_state === '已通过'
            })
          case '4':
            return this.tableData.filter(function (item) {
              return item.register_state === '未通过'
            })
        }
      }
    }
  }
</script>

