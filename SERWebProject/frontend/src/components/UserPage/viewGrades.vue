<template>
  <div>
    <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
      <el-tab-pane label="所有成绩" name="1"></el-tab-pane>
    </el-tabs>
    <!--<p>hello</p>-->
    <el-table
      :data="filteredTable"
      border
      :show-header="true"
      style="width: 100%">
      <el-table-column
        prop="pk"
        label="项目名称">
        <template scope="scope"> {{ scope.row.fields.registered_project_name||scope.row.fields.project_name}} </template>
      </el-table-column>
      <el-table-column
        prop="pk"
        label="团队项目"
        width="200px">
        <template scope="scope"> {{ scope.row.fields.if_group_project ? '是' : '否' }} </template>
      </el-table-column>

      <!--<el-table-column-->
        <!--prop="contact_info"-->
        <!--label="报名时间"-->
        <!--&gt;-->
        <!--<template scope="scope"> {{ scope.row.fields.register_datetime }} </template>-->
      <!--</el-table-column>-->
      <el-table-column
        prop="register_state"
        label="名次"
        width="200px">
        <template scope="scope">
          {{'第'+scope.row.fields.rank+'名'}}
          <!--{{approvalStatus(scope.row.fields.approval_status)}}-->
        </template>
      </el-table-column>
      <el-table-column
        label="成绩"
        width="200px">
        <template scope="scope">
          {{ scope.row.fields.grade }}
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
        tableData: []
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
            return this.tableData.filter(function (item) {
              return item.fields.if_finished
            })
          case '2':
            console.log(this.tableData)
            return null
//          case '3':
//            return this.tableData.filter(function (item) {
//              return item.register_state === '已通过'
//            })
//          case '4':
//            return this.tableData.filter(function (item) {
//              return item.register_state === '未通过'
//            })
        }
      }
    }
  }
</script>

