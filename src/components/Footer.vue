<script>
import { computed } from '@vue/runtime-core';
import {useStore} from 'vuex';
export default {
    setup(){
        const store = useStore();
        const isAbout = computed(()=>{
            return store.getters.isAbout;
        });

        return {isAbout}
    }
}
</script>

<template>
  <footer :class="{about:isAbout}">
        <span>Copyright © 2020 Rober Inc.</span>
        <span>Tel：0955699711&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mail：<a href="mailto:ecbr44@gmail.com">ecbr44@gmail.com</a></span>
    </footer>
</template>


<style lang="scss" scoped>
@import '~@/assets/scss/_mixins.scss';
footer{
    padding: 30px;
    font-size: 12px;
    color: $white;
    font-weight: 300;
    left:0;
    bottom: 0;
    z-index: 2;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: $full;
    flex-wrap: wrap;
    white-space: nowrap;
    position: relative;
    @include breakpoint(m){
        padding-top: 0;
    }
    span{
        display: inline-block;
        @include breakpoint(m){
            line-height: 25px;
        }
    }
    a{
        color: $white;
        &:hover{
            text-decoration: underline;
        }
    }
}
.about{
    position: absolute;
    bottom:30px;
    left:0;
    padding-bottom: 0;
    @include breakpoint(nbsm){
        bottom: 0;
        position: relative;
        padding-bottom: 30px;
        line-height: 27px;
    }
}
</style>