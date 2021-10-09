<script>
export default {

}
</script>

<template>
  <div class="login">
      <h1>登入</h1>
      <table class="form">
        <tr>
            <td>
                <input type="text" placeholder="帳號">
            </td>
        </tr>
        <tr>
            <td>
                <input type="password" placeholder="密碼">
            </td>
        </tr>
        <tr>
            <td>
                <a href="#">登入</a>
            </td>
        </tr>
      </table>
  </div>
</template>

<style scoped lang="scss">
@import '~@/assets/scss/_mixins.scss';

.login{
    max-width: 650px;
    width:$full;
    margin: 0 auto;
    background-color: rgba(255,255,255,0.1);
    border:1px solid $white;
    border-radius: 10px;
    padding:40px;
    position: relative;
    z-index: 5;
    margin-top: 100px;
    margin-bottom: 100px;
    h1{
        font-size: 30px;
        letter-spacing: 5px;
        text-align: center;
        color: $white;
        font-weight: 300;
        text-indent: -5px;
    }
    .form{
        width:$full;
        tr{
            td{
                padding-top: 20px;
                input{
                    width: $full;
                    height: 50px;
                    padding-left: 10px;
                    padding-right: 10px;
                    border-radius: 3px;
                }
                a{
                    display: block;
                    width:100px;
                    height: 40px;
                    border-radius: 3px;
                    text-align: center;
                    line-height: 40px;
                    font-size: 16px;
                    font-weight: 300;
                    background-color: $white;
                }
            }
        }
    }
}

</style>