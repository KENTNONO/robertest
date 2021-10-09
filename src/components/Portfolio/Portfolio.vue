<script>
import { computed, ref } from '@vue/reactivity';
import {useStore} from 'vuex';
import { onMounted, onUnmounted, watch } from '@vue/runtime-core';
export default {
    setup(){
        const store = useStore();

        const wrapper = ref(null);

        let boxIndex = -1;
        let timer = 0;

        const isLoad = computed(()=>store.getters.isLoad);

        const portfolioArr = computed(()=>{
            return store.getters.portfolioArr;
        });

        watch(isLoad,()=>{
            timer = setInterval(()=>{
                if(boxIndex < wrapper.value.children.length-1){
                    boxIndex++
                }else{
                    clearInterval(timer)
                }
                wrapper.value.children[boxIndex].classList.add('boxOpa');
            },300);
        });

        onUnmounted(()=>{
            clearInterval(timer);
            store.dispatch('handIsLoad',false)
        });

        const handImageLoad = (imgArr)=>{
            let i = 0;
            imgArr.forEach((image)=>{
                const imgs = new Image();
                imgs.src = image.img;
                imgs.addEventListener('load',()=>{
                i++;
                store.dispatch('handIsLoad',i===imgArr.length);
                // isLoad.value = i ===photo.arr.length;
                })
            })
        };

        const init = ()=>{
            store.dispatch('handInit').then(res=>{
                handImageLoad(res);
            })
        };

        onMounted(()=>{
            init();
        });

        

        return {isLoad,portfolioArr,wrapper}
    }
}
</script>

<template>
  <div ref="wrapper" class="wrapper">
        <div class="loading" v-if="!isLoad">
            <div class="lds-ring"><div></div><div></div><div></div><div></div></div>
        </div>
        <a v-for="(item) in portfolioArr" :href="item.url" :key="item.key" class="box" target="_blank">
            <img :src="item.img" alt="">
            <div class="title">{{item.name}}</div>
        </a>
    </div>
</template>

<style scoped lang="scss">
@import '~@/assets/scss/_mixins.scss';
.wrapper{
    position: relative;
    z-index: 3;
    padding: 60px 30px;
    display: grid;
    grid-gap: 20px;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
    grid-template-rows: auto;
    @include breakpoint(sPC){
        grid-template-columns: 1fr 1fr 1fr; 
    }
    @include breakpoint(m){
        grid-template-columns: 1fr 1fr;
        padding: 30px;
    }
    .loading{
        width: $full;
        height: $full;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        position: absolute;
        left:0;
        top:0;
        .lds-ring {
            display: inline-block;
            position: relative;
            width: 80px;
            height: 80px;
            margin-top: 50px;
          }
          .lds-ring div {
            box-sizing: border-box;
            display: block;
            position: absolute;
            width: 64px;
            height: 64px;
            margin: 8px;
            border: 8px solid #fff;
            border-radius: 50%;
            animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
            border-color: #fff transparent transparent transparent;
          }
          .lds-ring div:nth-child(1) {
            animation-delay: -0.45s;
          }
          .lds-ring div:nth-child(2) {
            animation-delay: -0.3s;
          }
          .lds-ring div:nth-child(3) {
            animation-delay: -0.15s;
          }
          @keyframes lds-ring {
            0% {
              transform: rotate(0deg);
            }
            100% {
              transform: rotate(360deg);
            }
          }
          
    }
    .box{
        display: block;
        opacity: 0;
        transition: 1.5s all;
        &:hover{
            img{
                filter:grayscale(0);
            }
        }
        img{
            display: block;
            width: $full;
            filter:grayscale(1);
            transition: 0.1s all;
        }
        .title{
            color: $white;
            font-size: 16px;
            font-weight: 400;
            padding-top: 5px;
        }
    }
    .boxOpa{
        opacity: 1;
    }
}
</style>