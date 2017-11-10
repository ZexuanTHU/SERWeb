<template>
  <div>
    <mheader></mheader>
    <h2 align="center">赛事查询</h2>
    <div class="selector">
      <el-form ref="form" :model="sizeForm" label-width="80px" size="mini"  :inline="true">
      <el-form-item label="比赛名称">
        <el-input v-model="sizeForm.name"></el-input>
      </el-form-item>
      <el-form-item label="活动区域">
        <el-select v-model="sizeForm.region" placeholder="请选择活动区域">
          <el-option label="区域一" value="shanghai"></el-option>
          <el-option label="区域二" value="beijing"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="活动时间">
        <el-col :span="11">
          <el-date-picker type="date" placeholder="选择日期" v-model="sizeForm.date1" style="width: 100%;"></el-date-picker>
        </el-col>
        <el-col class="line" :span="2">-</el-col>
        <el-col :span="11">
          <el-time-picker type="fixed-time" placeholder="选择时间" v-model="sizeForm.date2"
                          style="width: 100%;"></el-time-picker>
        </el-col>
      </el-form-item>
      <el-form-item label="活动性质">
        <el-checkbox-group v-model="sizeForm.type">
          <el-checkbox-button label="美食/餐厅线上活动" name="type"></el-checkbox-button>
          <el-checkbox-button label="地推活动" name="type"></el-checkbox-button>
          <el-checkbox-button label="线下主题活动" name="type"></el-checkbox-button>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="特殊资源">
        <el-radio-group v-model="sizeForm.resource" size="medium">
          <el-radio border label="线上品牌商赞助"></el-radio>
          <el-radio border label="线下场地免费"></el-radio>
        </el-radio-group>
      </el-form-item>
      <br>

    </el-form>
      <el-button type="primary" @click="search" style="float: right;margin-right: 200px">查询</el-button>
    </div>


        <!--<el-button>取消</el-button>-->
    <tableList></tableList>
  </div>
</template>

<script>
  import mheader from '../components/header'
  import tableList from './TableList.vue'

  export default {
    data () {
      return {
        sizeForm: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        }
      }
    },
    methods: {
      search () {
        console.log('submit!')
      }
    },
    components: {
      'mheader': mheader,
      'tableList': tableList
    },
    created: function () {
      if (this.$route.params.uid && localStorage.getItem('user_id') !== this.$route.params.uid) {
        this.$router.back()
      }
    }
  }
</script>
<style scoped>
  .selector {
    margin-top: 50px;
    margin-right: 40px;
    margin-left: 40px;
  }
</style>
