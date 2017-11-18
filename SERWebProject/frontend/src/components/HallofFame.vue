<template>
  <div>
    <mheader></mheader>
    <div class="w3-content" style="max-width:2000px;margin-top:6px">
      <div class="w3-container" style="width: 100%;min-height: 650px">
        <div class="w3-left" style="width: 200px;height: 100% ">
          <el-col :span="8">
            <h5></h5>
            <el-menu id="leftnav" default-active="4" class="el-menu-vertical-demo" @select="openPanel">

              <el-menu-item index="0"></el-menu-item>
              <el-menu-item index="1"></el-menu-item>
              <el-menu-item index="2"></el-menu-item>
              <el-menu-item index="3"></el-menu-item>
              <el-menu-item index="4"></el-menu-item>
            </el-menu>
          </el-col>
        </div>
        <div class="panel_content" style="margin-left: 200px; display: block; padding-top: 30px">
          <div class="w3-container panel"
               :style="{display:openedPanel==='0'?'inline-block':'none'}">
            <el-row>
              <el-col :span="8" v-for="field in hall_of_fame_data" :key="field.id">
                <el-card :body-style="{ padding: '0px' }" style="margin-top: 10px; width: 300px;">
                  <img @click="itemClicked(field)" :src="getImage(field.fields.HOF_image)" v-bind:alt="field" style="height: 300px;">
                  <div style="padding: 14px;">
                    <span> {{ field.fields.HOF_name }} </span>
                    <li> 性别 : {{ field.fields.HOF_gender }} </li>
                    <li> 级数 : {{ field.fields.HOF_selected_year }} </li>
                    <li> 班级 : {{ field.fields.HOF_class_id }} </li>
                    <li> 擅长项目 : {{ field.fields.HOF_expertise}} </li>
                  </div>
                  <el-dialog
                    :visible.sync="dialogVisible"
                    size="medium">
                    <h1> {{ name }}</h1>
                    <div>
                      <div style="float: right; margin-bottom: 100px">
                        <div v-if="loaded">
                          <img :src="getImage2(hof_img)" style="height: 300px;">
                        </div>
                      </div>
                      <div style="margin-right: 600px">
                        <el-tabs v-model="activeName" @tab-click="handleClick">
                          <el-tab-pane label="基本信息" name="first">
                            <li> 性别 : {{ gender }} </li>
                            <li> 级数 : {{ selected_year }} </li>
                            <li> 班级 : {{ class_id }} </li>
                            <li> 擅长项目 : {{ expertise}} </li>
                          </el-tab-pane>
                          <el-tab-pane label="个人简介" name="second">
                          {{ intro }}
                          </el-tab-pane>
                          <el-tab-pane label="个人荣誉" name="third">
                          {{ honor }}
                          </el-tab-pane>
                        </el-tabs>
                      </div>
                    </div>
                  </el-dialog>
                </el-card>
              </el-col>
            </el-row>
          </div>
        </div>
      </div>
    </div>
    <mfooter></mfooter>
  </div>
</template>

<script>
  import mheader from '@/components/header'
  import mfooter from '../components/mfooter'

  export default {
    data () {
      return {
        openedPanel: '0',
        activeName: 'first',
        dialogVisible: false,
        loaded: false,
        name: '',
        gender: '',
        selected_year: '',
        class_id: '',
        expertise: '',
        hof_img: '',
        intro: '',
        honor: '',
        hall_of_fame_data: [{
          fields: [{
            HOF_name: '',
            HOF_gender: '',
            HOF_selected_year: '',
            HOF_class_id: '',
            HOF_expertise: '',
            HOF_introduction: '',
            HOF_honor: '',
            HOF_image: ''
          }],
          pk: ''
        }]
      }
    },
    methods: {
      getData () {
        this.loaded = true
      },
      itemClicked: function (item) {
        this.getData()
        this.name = item.fields.HOF_name
        this.gender = item.fields.HOF_gender
        this.selected_year = item.fields.HOF_selected_year
        this.class_id = item.fields.HOF_class_id
        this.expertise = item.fields.HOF_expertise
        this.hof_img = item.fields.HOF_image
        this.intro = item.fields.HOF_introduction
        this.honor = item.fields.HOF_honor
        this.dialogVisible = true
      },
      openPanel: function (index) {
        this.openedPanel = index
      },
      handleClick (tab, event) {
        console.log(tab, event)
      },
      getImage (index) {
        var images = require.context('../assets/', true, /\.jpg$/)
        return images('./' + index)
      },
      getImage2 (index) {
        var images = require.context('../assets/', true, /\.jpg$/)
        return images('./' + index)
      },
      hall_of_fame_request () {
        this.$http.get('http://127.0.0.1:8000/api/hall_of_fame_request').then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.hall_of_fame_data = res['list']
          } else {
            this.$message.error('获取项目列表失败"')
            console.log(res['msg'])
          }
        })
      }
    },
    components: {
      'mheader': mheader,
      'mfooter': mfooter
    },
    created: function () {
      this.hall_of_fame_request()
      if (this.$route.params.uid && localStorage.getItem('user_id') !== this.$route.params.uid) {
        this.$router.back()
      }
    }
  }
</script>

<style scoped>
  @import url("//unpkg.com/element-ui@1.4.6/lib/theme-default/index.css");
  @import "../css/w3.css";
  @import "../css/user.css";

  a {
    text-decoration: none;
  }

  [v-cloak] {
    display: none;
  }
  #leftnav {
    margin-top: 40px;
    width: 200px;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }
</style>
