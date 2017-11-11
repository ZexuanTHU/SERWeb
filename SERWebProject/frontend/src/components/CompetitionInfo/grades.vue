<template>
  <el-table
    :data="tableData"
    style="width: 100%"
    :default-sort = "{prop: 'place', order: 'ascending'}"
    >
    <el-table-column
      prop="place"
      label="名次"
      width="180">
    </el-table-column>
    <el-table-column
      prop="name"
      label="姓名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="project"
      label="項目">
    </el-table-column>
    <el-table-column
      prop="other"
      label="備註">
    </el-table-column>
  </el-table>
</template>

<script>
  export default {
    data () {
      return {
        tableData: [{
          place: '1',
          name: '王小虎',
          project: '上海市普陀区金沙江路 1518 弄',
          other: '無'
        }, {
          place: '2',
          name: '王小虎',
          project: '上海市普陀区金沙江路 1517 弄',
          other: '無'
        }, {
          place: '3',
          name: '王小虎',
          project: '上海市普陀区金沙江路 1519 弄',
          other: '無'
        }, {
          place: '4',
          name: '王小虎',
          project: '上海市普陀区金沙江路 1516 弄',
          other: '無'
        }]
      }
    },
    methods: {
      formatter (row, column) {
        return row.project
      }
    }
  }
</script>