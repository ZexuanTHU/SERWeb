<template>
  <div>
    <mheader></mheader>
    <div class="w3-content" style="max-width:2000px;margin-top:6px">
      <div class="w3-container" style="width: 100%;min-height: 650px">
        <div class="w3-left" style="width: 200px;height: 100% ">
          <el-col :span="8">
            <h5></h5>
            <el-menu id="leftnav" default-active="4" class="el-menu-vertical-demo" @select="openPanel">

              <el-menu-item index="0">2013</el-menu-item>
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
              <el-col :span="8" v-for="(o, index) in 2" :key="o" :offset="index > 0 ? 2 : 0">
                <el-card :body-style="{ padding: '0px' }" style="margin-top: 10px">
                  <img @click="dialogVisible = true" src="../assets/halloffame.jpg" class="image">
                  <div style="padding: 14px;">
                    <span>李晨曦</span>
                  </div>
                </el-card>
              </el-col>
            </el-row>
            <el-dialog
              title="李晨曦"
              :visible.sync="dialogVisible"
              size="medium">
              <div>
                <div style="float: right; margin-bottom: 100px">
                  <img src="../assets/halloffame.jpg" style="display: block; max-width: 500px; max_height: 500px; width: auto; height: auto">
                </div>
                <div style="margin-right: 600px">
                  <el-tabs v-model="activeName" @tab-click="handleClick">
                  <el-tab-pane label="基本信息" name="first">
                    <ul v-for="item in items">
                      <li> 性别 : {{ item.gender }} </li>
                      <li> 级数 : {{ item.grade }} </li>
                      <li> 班级 : {{ item.class }} </li>
                      <li> 擅长项目 : {{ item.expertise }} </li>
                    </ul>
                  </el-tab-pane>
                  <el-tab-pane label="个人简介" name="second">
                    {{ intro }}
                  </el-tab-pane>
                  <el-tab-pane label="个人荣誉" name="third">
                    <ul v-for="award in awards">
                      <li> {{ award.first }} </li>
                      <li> {{ award.second }} </li>
                      <li> {{ award.third }} </li>
                      <li> {{ award.fourth }} </li>
                      <li> {{ award.fifth }} </li>
                      <li> {{ award.sixth }} </li>
                      <li> {{ award.seventh }} </li>
                    </ul>
                  </el-tab-pane>
                </el-tabs>
                </div>
              </div>
            </el-dialog>
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
        dialogVisible: false,
        activeName: 'first',
        hall_of_fame_data: [{
          fields: [{

          }],
          pk: ''
        }],
        items: [{
          name: '李晨曦',
          gender: '男',
          grade: '2013级',
          class: 'xx 班',
          expertise: '中长跑'
        }],
        intro: '李晨曦，清华大学计算机系2013级博士生，马拉松国家二级运动员，曾创下北京国际马拉松赛全程2小时51分18秒完赛的个人最佳成绩，42.195千米的赛道，平均每千米用时约4分4秒，被称为“清华马拉松第一人”，原虎扑翻译团版主、虎扑新声编辑。',
        awards: [{
          first: '2016年9月以2小时51分18秒创造清华大学在校普通生的马拉松最好成绩',
          second: '2016年5月代表清华大学参加New Balance中国大学生校园路跑接力赛总决赛获得冠军',
          third: '2016年9月代表清华大学参加耐克高校精英赛公路接力赛总决赛获得冠军并创造本届赛事普通生单棒最好成绩',
          fourth: '2016年4月参加清华大学“马约翰杯”学生田径运动会，获得男子甲组10000米和5000米双料冠军、4*800米接力第四、4*400米接力第五、师生异程接力第六',
          fifth: '2014年清华大学“马约翰杯”学生田径运动会万米接力冠军队成员、4*800米接力冠军',
          sixth: '2015年2月翻译出版了吉列姆.巴拉格所著的球星传记《梅西》',
          seventh: '2016年10月翻译出版了罗兰.拉赞比所著的球星传记《乔丹》'
        }]
      }
    },
    methods: {
      openPanel: function (index) {
        this.openedPanel = index
      },
      handleClick (tab, event) {
        console.log(tab, event)
      },
      hall_of_fame_request() {
        this.$http.get('http://127.0.0.1:8000/api/hall_of_fame_request').then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log('hello')
          console.log(res)
          if (res.error_num === 0) {
            this.carousel_img = res['list']
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
