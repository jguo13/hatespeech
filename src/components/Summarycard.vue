<template>
	  <div id="app">
      <div class= "row">
        <div class="image">
           <img :src="require(`@/assets/` + `${image_path}`)" width="100%" height="100%"/>
        </div>

  	    <div class="summary">
            <div class="heading">
            <h1> Introduction</h1>
            </div>
            <p class="intro"> {{ intro_paragraph }}</p>
  	    </div>
      </div>
	  </div>

</template>
<script>

export default {
	name: "Summarycard",
	props: {
		msg: String,
		date: String,
    image_path: String,
		subtitle: String,
    links: Array,
    intro_paragraph: String
	},

}
</script>
<style scoped>
/** {
  box-sizing: border-box;
}*/
/*
body {
  margin: 0;
  padding: 1px 0 0;
  width: 100vw;
  height: 100vh;
  background: #6B5CA5;
}*/

/*html {
  padding: 0;
  margin: 0;
}*/

#app{
  padding: 19px;
  display: flex;
/*  flex-direction: row;
*/

/*  flex-flow: row wrap;
*/  width: 100%;
  height: 100%;
}
.row{
  display:flex;
}
.image {
  outline-style: solid;
  outline-color: black;
  background-color: #FFAEBC;
  height: 100%;
  width: 50%;

}
.summary{
/*  height: 50%; */

  max-height: 100%;
  width: 50%;
  background: #f6cec4;
  outline-style: solid;
  outline-color: black;
  color: black;
/*  overflow: scroll;
  overflow-y: scroll;*/
}
.heading{
  outline-style: solid;
  background-color: #c5e2fc;
}
.intro{
  text-align: left;
  width: 100%;
  height: 100%;
  overflow: scroll;
  padding-left: 15px;
  padding-right: 15px;

/*  font-size: 17px;*/
  font-size: 2vmin;
  font-weight: bold;
  overflow-y: scroll;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;

}







</style>