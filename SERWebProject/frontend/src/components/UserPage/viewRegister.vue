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
        width="280px">
        <template scope="scope"> {{ scope.row.fields.registered_project_name || scope.row.fields.project_name }}
        </template>
      </el-table-column>
      <el-table-column
        prop="pk"
        label="项目类型"
        width="150px">
        <template scope="scope"> {{ scope.row.fields.if_group_project ? '团队' : '个人' }} </template>
      </el-table-column>

      <el-table-column
        prop="contact_info"
        label="队长"
        width="150px"
        >
        <template scope="scope"> {{ scope.row.fields.team_leader_name || '' }} </template>
      </el-table-column>
      <el-table-column
        prop="contact_info"
        label="报名时间"
        >
        <template scope="scope"> {{ scope.row.fields.register_datetime |formatDate }} </template>
      </el-table-column>
      <el-table-column
        prop="register_state"
        label="报名状态"
        width="150px">
        <template scope="scope">
          {{approvalStatus( scope.row.fields.approval_status)}}
        </template>
      </el-table-column>
      <el-table-column
        label="操作"
        width="110px"
        prop="register">
        <template scope="scope">
          <el-button type="text" size="small">
            <router-link :to="{name: 'project', params: {pid:scope.row.fields.project.toString(),uid:id.toString()}}">
              查看
            </router-link>
          </el-button>
          <span>/</span>
          <el-button type="text" size="small" @click="cancel(scope)">删除</el-button>
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
      cancel (scope) {
        console.log(scope.$index)
        this.$http.get('http://111.230.226.45:8888/api/project_registration_cancel_request/' + this.$route.params.uid + '/' + scope.row.fields.project).then((response) => {
//          var res = JSON.parse(response.bodyText)
          console.log(response)
          if (response.status >= 200 && response.status < 300) {
            if (response.bodyText === 'Canceled!') {
              this.$message('成功删除项目')
              this.tableData.splice(scope.$index, 1)
            } else {
              this.$message.error(response.bodyText)
            }
          } else {
            this.$message.error('删除请求失败"')
            console.log('failed')
          }
        })
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
    mounted: function () {

    },
    computed: {
      filteredTable: function () {
        switch (this.activeName.toString()) {
          case '1':
//            if (!this.tableData) return null
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

