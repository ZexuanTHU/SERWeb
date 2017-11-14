<template>
  <div>
    <mheader></mheader>
    <h2 align="center">赛事查询</h2>
    <div class="selector" style="width: 450px;border: 2px #edf0f5;    border-style: double;    border-radius: 20px;    position: relative;
    padding-top: 10px;">
      <el-form ref="form" :model="filterForm" label-width="80px" size="mini" :inline="true" align="left">
        <el-form-item label="比赛名称" prop="name">
          <el-input v-model="filterForm.name"></el-input>
        </el-form-item>
        <el-form-item label="团队项目">
          <el-select v-model="filterForm.isGroup" clearable placeholder="" style="width: 80px">
            <el-option label="是" value="true"></el-option>
            <el-option label="否" value="false"></el-option>
        </el-select>
      </el-form-item>
        <br>
        <!--<el-form-item label="活动时间">-->
        <!--<el-col :span="11">-->
        <!--<el-date-picker type="date" placeholder="选择日期" v-model="filterForm.date1" style="width: 100%;"></el-date-picker>-->
        <!--</el-col>-->
        <!--<el-col class="line" :span="2">-</el-col>-->
        <!--<el-col :span="11">-->
        <!--<el-time-picker type="fixed-time" placeholder="选择时间" v-model="filterForm.date2"-->
        <!--style="width: 100%;"></el-time-picker>-->
        <!--</el-col>-->
        <!--</el-form-item>-->
        <!--<el-form-item label="活动性质">-->
        <!--<el-checkbox-group v-model="filterForm.type">-->
        <!--<el-checkbox-button label="美食/餐厅线上活动" name="type"></el-checkbox-button>-->
        <!--<el-checkbox-button label="地推活动" name="type"></el-checkbox-button>-->
        <!--<el-checkbox-button label="线下主题活动" name="type"></el-checkbox-button>-->
        <!--</el-checkbox-group>-->
        <!--</el-form-item>-->
        <el-form-item label="报名状态">
          <el-radio-group v-model="filterForm.resource" size="medium">
            <el-radio border label="正在报名" value="1"></el-radio>
            <el-radio border label="即将开始" value="2"></el-radio>
            <el-radio border label="已经结束" value="3"></el-radio>

          </el-radio-group>
      </el-form-item>
      <br>
        <el-form-item style="position: relative;float: right"></el-form-item>

        <!--<el-button @click="resetForm('form')">重置</el-button>-->
    </el-form>
      <p align="right">
        <el-button type="primary" @click="search" style="position: relative">查询</el-button>
      </p>

    </div>


        <!--<el-button>取消</el-button>-->
    <!--<tableList></tableList>-->
    <div id="more news" style="margin: 0px 40px">
      <!--<h1 align="left">其他赛事</h1>-->
      <br/>
      <el-table
        :data="afterFiteredList"
        height=""
        border
        style="">
        <el-table-column
          prop="project_name"
          label="赛事名称"
          align="center">
          <template scope="scope"> {{ scope.row.fields.project_name }} </template>
        </el-table-column>
        <el-table-column
          prop="project_text"
          label="赛事简介"
          align="center">
          <template scope="scope"> {{ scope.row.fields.project_text }} </template>
        </el-table-column>
        <el-table-column
          prop="date"
          label="报名起止时间"
          align="center">
          <template scope="scope"> {{ scope.row.fields.pub_date }} -- {{ scope.row.fields.ddl_date }} </template>
        </el-table-column>
        <el-table-column
          prop="project_hot"
          label="当前报名人数"
          align="center">
          <template scope="scope"> {{ scope.row.fields.project_hot }} </template>
        </el-table-column>
        <el-table-column
          prop="max_reg"
          label="报名人数限制"
          align="center">
          <template scope="scope"> {{ scope.row.fields.max_reg }} </template>
        </el-table-column>
        <el-table-column
          prop="contact_name"
          label="紧急联系人姓名"
          align="center">
          <template scope="scope"> {{ scope.row.fields.contact_name }} </template>
        </el-table-column>
        <el-table-column
          prop="contact_tel"
          label="紧急联系人电话"
          align="center">
          <template scope="scope"> {{ scope.row.fields.contact_tel }} </template>
        </el-table-column>
        <el-table-column
          prop="register"
          label="赛事报名"
          align="center">
          <template scope="scope">
            <el-button size="mini">
              <p>一键报名</p>
            </el-button>
            <router-link :to="{name: 'project', params: {uid:$route.params.uid, pid: scope.row.pk}}">
              <el-button type="primary" size="mini">
                <p style="color: white">赛事详情</p>
              </el-button>
            </router-link>

          </template>
        </el-table-column>
      </el-table>
    </div>

  </div>
</template>

<script>
  import mheader from '../components/header'
  import tableList from './TableList.vue'

  export default {
    data () {
      return {
        filterForm: {
          name: '',
          isGroup: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        },
        latest_project_list: [{
          fields: {
            project_name: '',
            project_text: '',
            project_hot: '',
            ddl_date: '',
            group_project: '',
            pub_date: '',
            max_reg: '',
            contact_name: '',
            contact_tel: ''
          },
          pk: ''
        }],
        filterName: '',
        afterFiteredList: []
      }
    },
    methods: {
//      search () {
//        console.log('submit!')
//      },
      project_list_display () {
        this.$http.get('http://127.0.0.1:8000/api/project_list_display').then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            this.latest_project_list = res['list']
            this.afterFiteredList = this.latest_project_list
          } else {
            this.$message.error('获取项目列表失败"')
            console.log(res['msg'])
          }
        })
      },
      search () {
        var self = this
        this.afterFiteredList = this.latest_project_list.filter(function (item) {
          var correct = true
//          var correctTime, correctName, correctGroup
          if (self.filterForm.name) {
            var pattern = new RegExp(self.filterForm.name, 'g')
            if (!pattern.test(item.fields.project_name)) return false
          }
//          console.log(item.fields.project_name, pattern)
          var now = new Date()
          console.log(self.filterForm.resource)
          switch (self.filterForm.resource) {
            case '即将开始':
              correct = now < new Date(item.fields.pub_date)
              break
            case '已经结束':
              correct = now > new Date(item.fields.ddl_date)
              break
            case '正在报名':
              correct = now >= new Date(item.fields.pub_date) && now <= new Date(item.fields.ddl_date)
              break
            default:
          }
          if (!correct) return false
          if (self.filterForm.isGroup) {
            console.log(self.filterForm.isGroup, item.fields.group_project)
            correct = self.filterForm.isGroup === item.fields.group_project.toString()
          }
          return correct
        })
        console.log(this.afterFiteredList)
      }
//      resetForm(formName) {
//        this.$refs[formName].resetFields()
//        console.log(this.$refs[formName])
//      }

    },
//    computed: {
//      after_fitered_list: function () {
//        return
//      }
//    },
    created: function () {
      this.project_list_display()
      if (this.$route.params.uid && localStorage.getItem('user_id') !== this.$route.params.uid) {
        this.$router.back()
      }
    },
    components: {
      'mheader': mheader,
      'tableList': tableList
    }
  }
</script>
<style scoped>
  .selector {
    margin: 50px 40px;
    margin-bottom: 20px;
    /*margin-right: 40px;*/
    /*margin-left: 40px;*/
    padding-left: 20px;

  }
</style>
