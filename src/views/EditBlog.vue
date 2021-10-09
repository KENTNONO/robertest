<script>
import { onMounted, ref } from '@vue/runtime-core';
import { useEditor, EditorContent,FloatingMenu  } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import TextAlign from '@tiptap/extension-text-align';
import TextStyle from '@tiptap/extension-text-style';
import { Color } from '@tiptap/extension-color';
import Image from '@tiptap/extension-image';
import Bold from '@tiptap/extension-bold';
import Italic from '@tiptap/extension-italic';
import Link from '@tiptap/extension-link'
import Strike from '@tiptap/extension-strike'

export default {
    components: {
        EditorContent,
        FloatingMenu
    },
    setup(){

        const editor = useEditor({
            content: '<p>I’m running tiptap with Vue.js. 🎉</p>',
            extensions: [
                StarterKit,
                TextStyle,
                Color,
                Image,
                Bold,
                Link,
                Italic,
                Strike,
                TextAlign.configure({
                    types: ['heading', 'paragraph'],
                }),
            ],
        })

        const handCkData = ()=>{
            // console.log(editor.value.options.content);
            console.log(editor.value.getHTML());
        };

        const addImage = ()=>{
            const url = window.prompt('URL')

            if (url) {
                editor.value.chain().focus().setImage({ src: url }).run()
            }
        };

        const setLink = ()=>{
            const url = window.prompt('URL')

            editor.value
                .chain()
                .focus()
                .extendMarkRange('link')
                .setLink({ href: url })
                .run()
            
        };

        onMounted(()=>{
            console.log(editor);
        })
        

        return {
            handCkData,
            editor,
            addImage,
            setLink
        }
    }
}
</script>

<template>
  <div class="edit">
      <table>
          <tr>
              <td>
                  <input class="textInput" type="text" placeholder="請輸入標題">
              </td>
          </tr>
          <tr>
              <td>
                  <input class="textInput" type="text" placeholder="描述">
              </td>
          </tr>
          <tr>
              <td>
                  <select>
                      <option>全部文章</option>
                      <option>網頁知識</option>
                      <option>網頁技術分享</option>
                      <option>電影哈拉</option>
                      <option>NBA反指標</option>
                      <option>生活來打屁</option>
                  </select>
              </td>
          </tr>
          <tr>
              <td>
                  <input class="textInput" type="date">
              </td>
          </tr>
          <tr>
              <td>
                  <ul>
                      <li><input name="001" id="r1" type="radio"><label for="r1">發佈</label></li>
                      <li><input name="001" id="r2" type="radio"><label for="r2">不發佈</label></li>
                  </ul>
              </td>
          </tr>
          <tr>
              <td>
                  <input type="file" class="fileUpload" name="" id="">
                  <button>上傳圖片</button>
              </td>
          </tr>
          <tr>
              <td>
                  <div v-if="editor">
                        <button @click="addImage">新增圖片</button>
                        <button @click="editor.chain().focus().toggleBold().run()" :class="{ 'is-active': editor.isActive('bold') }">
      bold
    </button>
    <button @click="editor.chain().focus().toggleItalic().run()" :class="{ 'is-active': editor.isActive('italic') }">
      italic
    </button>
    <button @click="setLink" :class="{ 'is-active': editor.isActive('link') }">
      link
    </button>
    <button @click="editor.chain().focus().unsetLink().run()" v-if="editor.isActive('link')">
      remove
    </button>
    <button @click="editor.chain().focus().toggleStrike().run()" :class="{ 'is-active': editor.isActive('strike') }">
      strike
    </button>
                        <input type="color" @input="editor.chain().focus().setColor($event.target.value).run()" :value="editor.getAttributes('textStyle').color" />
                        <button @click="editor.chain().focus().setTextAlign('left').run()" :class="{ 'is-active': editor.isActive({ textAlign: 'left' }) }">left</button>
                        <button @click="editor.chain().focus().setTextAlign('center').run()" :class="{ 'is-active': editor.isActive({ textAlign: 'center' }) }">center</button>
                        <button @click="editor.chain().focus().setTextAlign('right').run()" :class="{ 'is-active': editor.isActive({ textAlign: 'right' }) }">right</button>
                        <button @click="editor.chain().focus().setTextAlign('justify').run()" :class="{ 'is-active': editor.isActive({ textAlign: 'justify' }) }">justify</button>
                        <button @click="editor.chain().focus().unsetTextAlign().run()">set default</button>
                        <floating-menu :editor="editor" v-if="editor">
                            <button @click="editor.chain().focus().toggleHeading({ level: 1 }).run()" :class="{ 'is-active': editor.isActive('heading', { level: 1 }) }">h1</button>
                            <button @click="editor.chain().focus().toggleHeading({ level: 2 }).run()" :class="{ 'is-active': editor.isActive('heading', { level: 2 }) }">h2</button>
                            <button @click="editor.chain().focus().toggleBulletList().run()" :class="{ 'is-active': editor.isActive('bulletList') }">bullet list</button>
                        </floating-menu>
                        <editor-content :editor="editor" />
                    </div>
              </td>
          </tr>
          <tr>
              <td>
                  <a href="#" class="btn send" @click="handCkData">送出</a>
                  <a href="#" class="btn back">返回</a>
              </td>
          </tr>
      </table>
  </div>
</template>
<style scoped lang="scss">
@import '~@/assets/scss/_mixins.scss';
/deep/ .ProseMirror{
    background-color: #fff;
    padding: 10px;
    height: 300px;
    overflow:auto;
    img{
        max-width: $full;
    }
    a{
        text-decoration: underline;
    }
}
.fileUpload{
    color: #fff;
}
.edit{
    max-width: 800px;
    width:$full;
    margin: 0 auto;
    position: relative;
    z-index: 2;
    :deep(.ck-editor__editable){
        height: 300px;
    }
    table{
        width:$full;
        tr{
            td{
                padding-bottom: 20px;
                .textInput{
                    width: $full;
                    height: 40px;
                    padding-left: 7px;
                    padding-right: 7px;
                    
                }
                select{
                    width: $full;
                    height: 40px;
                    padding-left: 7px;
                    padding-right: 7px;
                }
                ul{
                    li{
                        display: inline-block;
                        margin-right: 10px;
                        color: $white;
                        font-size: 16px;
                        input{
                            margin-right: 5px;
                        }
                    }
                }
                .btn{
                    display: inline-block;
                    margin-right: 10px;
                    border-radius: 3px;
                    padding: 7px 25px;
                    font-size: 16px;
                }
                .send{
                    background-color:$white ;
                }
                .back{
                    background-color: #bbb;
                }
            }
        }
    }
}

</style>