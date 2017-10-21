<template>
    <el-form :model="ruleForm2" :rules="rules2" ref="ruleForm2" label-width="120px" id="login">
      <el-form-item  prop="username">
        <el-input placeholder="Username"  v-model="ruleForm2.checkPass" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item prop="pass">
        <el-input placeholder="Password" type="password" v-model="ruleForm2.pass" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm2')">Login</el-button>
      </el-form-item>
    </el-form>
</template>

<script>
  export default {
    data () {
      var Username = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('Please input username'))
        }
        setTimeout(() => {
          if (!Number.isInteger(value)) {
            callback(new Error('Please input digits'))
          } else {
            if (value < 18) {
              callback(new Error('Age must be greater than 18'))
            } else {
              callback()
            }
          }
        }, 1000)
      }
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Please input the password'))
        } else {
          if (this.ruleForm2.checkPass !== '') {
            this.$refs.ruleForm2.validateField('checkPass')
          }
          callback()
        }
      }

      return {
        ruleForm2: {
          pass: '',
          checkPass: '',
          age: ''
        },
        rules2: {
          pass: [
            { validator: validatePass, trigger: 'blur' }
          ],
          age: [
            { validator: Username, trigger: 'blur' }
          ]
        }
      }
    },
    methods: {
      submitForm (formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!')
          } else {
            console.log('error submit!!')
            return false
          }
        })
      }
    }
  }
</script>

<style scoped>
  @import url("//unpkg.com/element-ui@1.4.7/lib/theme-default/index.css");

  #login {
    max-width: 350px;
    margin: auto;
    padding: 50px;
    box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
  }

  .el-form-item {
    margin-left: -120px;
  }

  .el-button {
    width: 100%;
  }

</style>
