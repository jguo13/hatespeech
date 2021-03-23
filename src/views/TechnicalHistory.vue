<template>
  <div class="about">
<!-- 		<div> <particles-bg type="cobweb" :bg="true" /> </div> -->
	<div class="summarycards">
		<Summarycard image_path="facebook.png" intro_paragraph="Scraping has been used in Journalism to enhance stories, audit big tech industries, and expose governmental flaws. The following stories show the power that being able to scrape websites have--it is a way to cover more ground than you humanely can, and a way to gather data for meaningful analysis. However it doesn’t come without risk--when you scrape a website you should always prepare yourself for a cease & desist letter should you be found out. That being said, there are methods detailed below that can mitigate your risk. "/>

	</div>
	<div class="historycards">

	<div class="row1">
	<FlipCard date="2018" subtitle="Doctors & Sex Abuse" msg="Projects in Journalism that involve scraping are often referred to as “boutique” projects. They are tailor made for a specific project/website and retired after the project is published. This is one of those stories, however it shows the importance that scraping can have. In this Atlanta Journal-Constitution story, journalists found how doctors who sexually abuse their patients are often able to escape punishment, continue practicing medicine, and continue their patterns of abuse on future patients. Part of the reason this phenomena exists is that if a doctor has sexually abused their patient but then switches state to practice medicine, you would have to go to their former state county’s medical board website to search through the records. The journalists at AJC built custom web scrapers for different medical board websites around the country to retrieve the allegations of sexual misconduct, and then used machine learning to classify these allegations, reducing the time the journalists needed to spend to manually go through each document. 
" :links="['https://doctors.ajc.com/']"/>



<!-- 	</div>
	<div class="row1"> -->
		<FlipCard date="2020" subtitle="Google’s Top Search Result? Surprise! It’s Google" msg="	In this story for the Markup, journalists Adrianne Jeffries and Leon Yin were interested in finding out what Google’s top search result was. To do so, they created a sample of over 10,000 searches via web scraping, and analyzed the results. They were also able to use a mobile emulator to see how the Google results looked on an iPhone, allowing for even finer-grain analysis. To create this project, they focused on creating simple scripts that could run on a single laptop. Doing anything greater might be halted both through anti-scraping measures Google has pre-baked in their webpages and might start to get them in trouble legally. However even with these simple scripts, they were able to audit a large technology company in a way that has not been done before." :links="['https://themarkup.org/google-the-giant/2020/07/28/google-search-results-prioritize-google-products-over-competitors']"/>

	<FlipCard date="2020" subtitle="Online Political Ads Transparency Project" msg="In September of 2020, the NYU Ad Observatory launched a project to track the political
ads that Facebook was showing users amid the 2020 presidential election. The year before, Facebook had launched its ad library in response to complaints that it was partly to blame for the disinformation campaigns that plagued the 2016 election. The ad library was released as a way to bring transparency into its ad-buying process. However since its release, it’s also been mired in controversy. Along with its ui, it released an api that was reported to not only be buggy, but also so buggy that it was impossible to file new bugs. The NYU project, which did not create autonomous scrapers but rather recruited over 6,000 volunteers to use a chrome extension as they browsed Facebook, found that there were discrepancies between the ads that users saw and the ads that were reported on the Ad Library. In October, Facebook sent them a cease and desist letter which included the deletion of all their currently collected data. The issue blew up--then democrat presidential nominee candidate Amy Klobuchar even tweeted in solidarity with NYU, calling for Facebook to be more transparent in their advertisements. NYU’s work is an important lesson in any project that includes data collection on a large tech company. These tech companies are usually well funded and do not mind the money or time resources it takes to bury you in law suits. As such, you need to set yourself up for defense--the more minimally autonomous you can make your data collection (ie browser extension over autonomous scraper), the better. The more protected you can make the user’s whose data you are collecting, the better. Technology has become so advanced that the most important decision you end up making may be what you choose not to do versus what you can do." :links="['https://engineering.nyu.edu/research/online-political-ads-transparency']"/>



	</div>
	</div>
  </div>

</template>

<script>
// import Historycards from "../components/Historycards"
import Summarycard from "../components/Summarycard"
import FlipCard from "../components/FlipCard"
// import Cards from "../components/Cards"
// import Arrows from "../components/Arrow"
export default {
  components: {
  	// Historycards,
  	Summarycard,
  	FlipCard,
  	// Cards,
   }
}
</script>

<style scoped>

.row1{
	display: flex;
	width: 100%;
	flex-flow: row wrap;
	justify-content: space-around;

/*	grid-auto-flow: column;
*/
/*	grid-column: 1/-1;*/
/*	grid-auto-flow: column;
*/}
.summary{
	display: grid;
	grid-auto-flow: column;
	justify-content: right;
}
body {

  background-color: #FFD662FF;
}

.historycards {
	display: flex;
	flex-direction: row;
	flex-flow: row wrap;
	width: 100%;
	justify-content: center;



}
.topbanner {
	background: beige;
}


</style>
