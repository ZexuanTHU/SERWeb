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
              <el-col :span="8" v-for="field in school_team_data" :key="field.id">
                <el-card :body-style="{ padding: '0px' }" style="margin-top: 10px; width: 300px;">
                  <img @click="itemClicked(field)" :src="getImage(field.fields.school_team_image)" v-bind:alt="field" style="height: 300px;">
                  <div style="padding: 14px;">
                    <span> {{ field.fields.school_team_name }} </span>
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
                          <el-tab-pane label="队伍成员" name="first">
                            <p><span v-html="member"></span></p>
                          </el-tab-pane>
                          <el-tab-pane label="队伍简介" name="second">
                            {{ intro }}
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
        school_team_img: '',
        member: '',
        intro: '',
        school_team_data: [{
          fields: [{
            school_team_name: '',
            school_team_gender: '',
            school_team_introduction: '',
            school_team_member: '',
            school_team_image: ''
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
        this.name = item.fields.school_team_name
        this.gender = item.fields.school_team_gender
        this.hof_img = item.fields.school_team_image
        this.intro = item.fields.school_team_introduction
        this.member = item.fields.school_team_member
        this.stringData(this.member)
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
      stringData (data) {
        var str = data.replace(/\n/g, '<br />')
        this.member = str
      },
      school_team_request () {
        this.$http.get('http://111.230.226.45:8888/api/school_team_request').then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.school_team_data = res['list']
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
      this.school_team_request()
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
