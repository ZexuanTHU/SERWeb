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
                  <img @click="dialogVisible = true" src="../assets/schoolteam.jpg" class="image">
                  <div style="padding: 14px;">
                    <span>计算机系女篮</span>
                  </div>
                </el-card>
              </el-col>
            </el-row>
            <el-dialog
              title="计算机系女篮"
              :visible.sync="dialogVisible"
              size="medium">
              <div>
                <div style="float: right; margin-bottom: 100px">
                  <img src="../assets/schoolteam.jpg" style="display: block; max-width: 500px; max_height: 500px; width: auto; height: auto">
                </div>
                <div style="margin-right: 600px">
                  <el-tabs v-model="activeName" @tab-click="handleClick">
                    <el-tab-pane label="队伍成员" name="first">
                      <ul v-for="item in items">
                        <li> 教练 : {{ item.coach }} </li>
                        <li> 队长 : {{ item.leader }} </li>
                        <li> 队员 : {{ item.member }} </li>
                      </ul>
                    </el-tab-pane>
                    <el-tab-pane label="队伍简介" name="second">
                      {{ intro }}
                    </el-tab-pane>
                    <!--<el-tab-pane label="个人荣誉" name="third">-->
                      <!--<ul v-for="award in awards">-->
                        <!--<li> {{ award.first }} </li>-->
                        <!--<li> {{ award.second }} </li>-->
                        <!--<li> {{ award.third }} </li>-->
                        <!--<li> {{ award.fourth }} </li>-->
                        <!--<li> {{ award.fifth }} </li>-->
                        <!--<li> {{ award.sixth }} </li>-->
                        <!--<li> {{ award.seventh }} </li>-->
                      <!--</ul>-->
                    <!--</el-tab-pane>-->
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
        items: [{
          coach: '贾佳欣',
          leader: '张子薇',
          member: '王苜子 范佳悦 徐玥 张一铭 童皓玥 林敏 孟昕悦 吴玥仪 张晨 王焱 周素平'
        }],
        intro: '2015年建队，队伍成员不仅有充满活力的本科生，还有球场经验老道的研究生学姐。虽然队史不长，但贵系女篮在马杯赛事上敢打敢拼，已经成为了一支不容小觑的新生力量'
      }
    },
    methods: {
      openPanel: function (index) {
        this.openedPanel = index
      },
      handleClick (tab, event) {
        console.log(tab, event)
      }
    },
    components: {
      'mheader': mheader,
      'mfooter': mfooter
    },
    created: function () {
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
