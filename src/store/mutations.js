export default{
    init(state,payload){
        state.portfolioArr = payload.portfolio;
    },
    blogData(state,payload){
        state.blogData = payload
    },
    classIdx(state,num){
        state.classIdx = num;
    },
    handBlogList(state,payload){
        state.categoryArr = payload;
        state.blogListArr = payload;
    },
    handCategoryArr(state,strCategory){
        state.categoryArr = state.blogListArr.filter((item)=>{
            if(strCategory !== ''){
                return item.kind === strCategory;
            }else{
                return state.blogListArr
            }
        });
    },
    categoryKind(state,categoryKind){
        state.categoryKind = categoryKind;
    },
    handIsLoad(state,bool){
        state.isLoad = bool
    },
    handIsMenu(state,bool){
        state.isMobileMenu = bool;
    },
    handIsAboutFalse(state,bool){
        state.isAbout = bool
    },
    handIsAboutTrue(state,bool){
        state.isAbout = bool
    },
}