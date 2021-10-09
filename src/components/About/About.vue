<script>
export default {

}
</script>

<template>
  <div class="main">
        <div class="container">
            <h1>您好，我叫羅拔~</h1>
            <div class="bb">
                <b>經歷</b>
                <ul class="smallTxt">
                    <li>宏碁資訊服務-多媒體設計師暨前端工程師</li>
                    <li>康泰納仕VOGUE雜誌-數位設計既前端工程師</li>
                    <li>毅達創意-網頁設計師</li>
                    <li>長榮集團-數位講師</li>
                    <li>商業週刊-長期配合網頁設計師暨前端工程師</li>
                    <li>蕾黛絲-長期配合前端工程師</li>
                    <li>聚思文創-長期配合網頁設計師暨前端工程師</li>
                    
                </ul>
            </div>
            <div class="bb">
                <b>技能</b>
                <ul class="smallTxt">
                    <li>
                        設計軟體
                        <br>Illustrator、Photoshop 、Animate CC、Dreamweaver、XD
                    </li>
                    <li>
                        前端工具<br>
                        Visual Studio Code、HTML、CSS、SCSS、Javascript、jQuery、Git
                    </li>
                </ul>
            </div>
            <div class="bb">
                <b>學歷</b>
                <ul class="smallTxt">
                    <li>
                        台灣科技大學 設計系研究所(假日在職就讀中)
                    </li>
                    <li>
                        醒吾科技大學 資訊傳播系(肄)
                    </li>
                    <li>復興商工 廣告設計系(畢)</li>
                </ul>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import '~@/assets/scss/_mixins.scss';
.main{
    padding:60px 30px;
    position: relative;
    z-index: 3;
    @include breakpoint(nbsm){
        padding: 30px;
    }
    .container{
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;
        align-content: flex-start;
        align-items: flex-start;
        max-width: 1200px;
        margin: 0 auto;
        h1{
            font-size: 35px;
            letter-spacing: 1px;
            font-weight: 400;
            color: $white;
            width: $full;
            padding-bottom: 10px;
            border-bottom: 1px solid $white;
        }
        .bb{
            padding-top: 50px;
            width: $full / 2;
            display: flex;
            align-items: flex-start;
            @include breakpoint(nbsm){
                width: $full;
            }
            b{
                white-space: nowrap;
                margin-right: 40px;
                font-weight: 400;
                color: $white;
                font-size: 30px;
                letter-spacing: 1px;
                padding-bottom: 10px;
            }
            .smallTxt{
                li{
                    font-size: 16px;
                    font-weight: 300;
                    color: $white;
                    letter-spacing: 1px;
                    line-height: 28px;
                    padding-bottom: 7px;
                    list-style-type: disc;
                    margin-left: 23px;
                    @include breakpoint(nbsm){
                        padding-bottom: 10px;
                    }
                    &:last-child{
                        padding-bottom: 0;
                    }
                }
            }
        }
    }
}
</style>