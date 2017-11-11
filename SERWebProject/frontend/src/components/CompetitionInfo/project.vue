<template>
  <div id="project">
    <mheader></mheader>
    <!-- Page content -->
    <div class="w3-content" style="max-width:2000px;margin-top:6px">
      <div class="w3-container" style="width: 100%;min-height: 650px">
        <div class="w3-left" style="width: 200px;height: 100% ">
          <el-col :span="8">
            <h5></h5>
            <el-menu id="leftnav" default-active="4" class="el-menu-vertical-demo" @select="openPanel">
              <el-menu-item index="1">赛事资讯</el-menu-item>
              <el-menu-item index="2">比赛成绩</el-menu-item>
            </el-menu>
          </el-col>
        </div>
        <div class="panel_content" style="margin-left:200px;display: block;padding-top:30px">
          <div id="view_register" class="w3-container panel "
               :style="{display:openedPanel==='1'?'inline-block':'none'}">
            <competitionInfo></competitionInfo>
          </div>
          <div id="view_grades" class="w3-container panel "
               :style="{display:openedPanel==='2'?'inline-block':'none'}">
            <grades></grades>
          </div>
        </div>
      </div>
      <mfooter></mfooter>
    </div>
  </div>
</template>

<script>
  import mheader from '../header.vue'
  import mfooter from '../mfooter.vue'
  import competitionInfo from './CompetitionInfo.vue'
  import grades from './grades.vue'
  export default {
    data () {
      return {
        openedPanel: '1'
      }
    },
    created: function () {
      window.scrollTo(0, 0)
    },
    methods: {
      openPanel: function (index) {
        this.openedPanel = index
      }
    },
    components: {
      'mheader': mheader,
      'mfooter': mfooter,
      'competitionInfo': competitionInfo,
      'grades': grades
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @import url("//unpkg.com/element-ui@1.4.6/lib/theme-default/index.css");
  @import "../../css/w3.css";
  @import "../../css/user.css";

  a {
    text-decoration: none;
  }

  #leftnav {
    margin-top: 40px;
    width: 200px;
  }

</style>


