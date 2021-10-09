<script>
import { computed, onMounted, onUnmounted } from '@vue/runtime-core';
import {useRoute,useRouter} from 'vue-router';
import {useStore} from 'vuex';
export default {
    setup(){
        const route = useRoute();
        const router = useRouter();
        const store = useStore();
        let timer = 0;

        const blogData = computed(()=>{
            return store.getters.blogData;
            console.log(store.getters.blogData);
        });

        const backPage = ()=>{
            router.go(-1)
        };

        onMounted(()=>{
            const id = route.params.id
            store.dispatch('blogData',id).then((res)=>{
                if(res === 404){
                    timer = setTimeout(()=>{
                        router.push({path:"/blog"});
                    },3000)
                }
            });
        });

        onUnmounted(()=>{
            clearTimeout(timer);
        })

        return{
            blogData,
            backPage
        }
    }
}
</script>

<template>
    <div class="blogInner">
        <div class="info">
            <div class="time">{{blogData.time}}</div>
            <div class="kind">{{blogData.kind}}</div>
        </div>
        <div class="title">{{blogData.title}}</div>
        <div class="ckEditor" v-html="blogData.html">
        </div>
        <div class="underCtrl">
            <div class="share">
                <a href="#" class="fb">
                    <img src="~@/assets/img/fb.svg" alt="">
                </a>
                <a href="#" class="line">
                    <img src="~@/assets/img/line.svg" alt="">
                </a>
            </div>
            <a href="#" class="backBtn" @click.prevent="backPage">返回上一頁</a>
        </div>
    </div>
</template>

<style lang="scss" scoped>
    @import '~@/assets/scss/_mixins.scss';
    .blogInner{
        width:$full;
        @include breakpoint(nb){
            margin-left: 0;
        }
        .info{
            @include breakpoint(nb){
                padding-top: 30px;
            }
            .time{
                display: inline-block;
                margin-right: 15px;
                color: $white;
                font-size: 14px;
                font-weight: 100;
            }
            .kind{
                display: inline-block;
                font-size: 14px;
                color: $white;
                letter-spacing: 1px;
                font-weight: 100;
            }
        }
        .title{
            font-size: 30px;
            line-height: 40px;
            color: $white;
            letter-spacing: 1px;
            padding-top: 5px;
            font-weight: 300;
        }
        .ckEditor{
            font-size: 18px;
            letter-spacing: 1px;
            color: $white;
            font-weight: 100;
            :deep(img){
                width: $full;
            }
        }
        .underCtrl{
            display: flex;
            justify-content: space-between;
            align-items: center;
            width:$full;
            padding-top: 40px;
            .share{
                a{
                    margin-right: 30px;
                    display: inline-block;
                    img{
                        width:30px;
                    }
                }
            }
            .backBtn{
                font-size: 15px;
                letter-spacing: 1px;
                font-weight: 100;
                color: $white;
                text-decoration: underline;
                &:hover{
                    text-decoration: none;
                }
            }
        }
    }
</style>>
