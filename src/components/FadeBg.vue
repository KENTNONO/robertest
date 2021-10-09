

<script>
import { onMounted, ref } from '@vue/runtime-core'
export default {
    setup(){

        const fadeBg = ref(null);
        let timer = 0;
        let index = 0;

        onMounted(()=>{
            timer = setInterval(()=>{
                if(index < 3){
                    index++
                }else{
                    index = 0;
                }
                for(let i = 0; i < fadeBg.value.children.length; i++){
                    fadeBg.value.children[i].classList.remove('current')
                }
                fadeBg.value.children[index].classList.add('current')
            },3000);
        });

        return{fadeBg}
    }
}
</script>

<template>
  <div class="dot"></div>
    <div ref="fadeBg" class="fadeBg">
        <div class="current"></div>
        <div></div>
        <div></div>
        <div></div>
    </div>
</template>

<style lang="scss" scoped>
@import '~@/assets/scss/_mixins.scss';
.dot{
    position: fixed;
    left:0;
    top:0;
    z-index: 2;
    width: $full;
    height: $full;
    background-image: url('~@/assets/img/dots.png');
}
.fadeBg{
    position: fixed;
    left:0;
    top:0;
    z-index: 1;
    width: $full;
    height: $full;
    >div{
        width: $full;
        height: $full;
        position: absolute;
        left:0;
        top:0;
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        opacity: 0;
        transition: 0.8s opacity;
        animation: scale 8s linear infinite alternate;
        &:nth-child(1){
            background-image: url('~@/assets/img/s1.png');
        }
        &:nth-child(2){
            background-image: url('~@/assets/img/s2.png');
        }
        &:nth-child(3){
            background-image: url('~@/assets/img/s3.png');
        }
        &:nth-child(4){
            background-image: url('~@/assets/img/s4.png');
        }
    }
    >.current{
        opacity: 1;
    }
}

@keyframes scale{
    0%{
        transform: scale(1);
    }
    100%{
        transform: scale(1.1);
    }
}
</style>