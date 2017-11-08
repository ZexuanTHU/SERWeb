<template>
  <div>
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
        prop="pk"
        label="项目名称"
        width="180px">
        <template scope="scope"> {{ scope.row.fields.registered_project_name }} </template>
      </el-table-column>
      <el-table-column
        prop="pk"
        label="团队项目"
        width="100px">
        <template scope="scope"> {{ '是' }} </template>
      </el-table-column>

      <el-table-column
        prop="contact_info"
        label="报名时间"
        >
        <template scope="scope"> {{ scope.row.fields.register_datetime }} </template>
      </el-table-column>
      <el-table-column
        prop="register_state"
        label="报名状态"
        width="100">
        <template scope="scope">
          {{approvalStatus( scope.row.fields.approval_status)}}
        </template>
      </el-table-column>
      <el-table-column
        label="报名状态"
        width="100"
        prop="register">
        <template scope="scope">
          <el-button type="text" size="small">
            <router-link :to="{name: 'CompetitionInfo', params: {pid:scope.row.fields.project.toString()}}">
              查看
            </router-link>
            /删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>

</template>

<script>
  export default {
    data () {
      return {
        id: this.$route.params.uid,
        activeName: '1',
        tableData: [
          {
            'model': 'backend.projectregisterrelationship',
            pk: 9,
            'fields': {
              'user': 22,
              'user_info': 8,
              'register_name': '叶泽轩',
              'student_id': '2014012430',
              'project': 2,
              'registered_project_name': '女子100m',
              'register_datetime': '2017-11-06T11:03:27.747Z',
              'approval_status': 'PE',
              'grade': '完赛',
              'if_finished': false
            }
          },
          {
            'model': 'backend.projectregisterrelationship',
            'pk': 8,
            'fields': {
              'user': 22,
              'user_info': 8,
              'register_name': '叶泽轩',
              'student_id': '2014012430',
              'project': 1,
              'registered_project_name': '男子100m',
              'register_datetime': '2017-11-06T11:03:24.172Z',
              'approval_status': 'PE',
              'grade': '完赛',
              'if_finished': false
            }
          }
        ]
      }
    },
    methods: {
      handleClick (row) {
        console.log(this.activeName.toString())
      },
      malert (row) {
        alert(row.project_name)
      },
      approvalStatus (status) {
        switch (status) {
          case 'PE':
            return '审核中'
          case 'AP':
            return '已通过'
          case 'RE':
            return '未通过'
        }
      }
    },
    created: function () {
      this.$http.get('http://localhost:8000/api/project_register_relationship_request/' + this.id).then((response) => {
        var res = JSON.parse(response.bodyText)
        console.log(res)
        if (res.error_num === 0) {
          this.tableData = res.list
        } else {
          this.$message.error('获取个人信息列表失败"')
          console.log(res['msg'])
        }
      })
    },
    computed: {
      filteredTable: function () {
        switch (this.activeName.toString()) {
          case '1':
            console.log(this.activeName, this.tableData)
            return this.tableData
          case '2':
            return this.tableData.filter(function (item) {
              return item.fields.approval_status === 'PE'
            })
          case '3':
            return this.tableData.filter(function (item) {
              return item.fields.approval_status === 'AP'
            })
          case '4':
            return this.tableData.filter(function (item) {
              return item.fields.approval_status === 'RE'
            })
        }
      }
    }
  }
</script>

<style scoped>
  a {
    text-decoration: none;
  }

</style>

