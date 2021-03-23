<template>
  <div class="about">
<!-- 		<div> <particles-bg type="cobweb" :bg="true" /> </div> -->
	<div class="summarycards">
		<Summarycard image_path="ip.png" intro_paragraph="If you choose to create a scraping project, there are several technical factors that you need to be aware of, primarily involving the anti-scraping measurements that companies employ on their websites. Most of these anti-scraping measurements stem from the desire to keep bots out of their servers so they do not jam up traffic and thus slow down service to legitimate users and customers. The following sections will detail the technical aspects that you need to consider to make your project leave a minimal, discreet footprint."/>

	</div>
	<div class="historycards">

	<div class="row1">
	<FlipCard date="" subtitle="Masking the IP Address" msg="The most common anti-scraping measure is black-listing an IP address that exceeds a certain request rate threshold, or which overall exhibits a suspicious pattern of activity. An IP address stands for Internet Protocol Address. Usually, when you connect to wifi, you are not technically connected to the internet directly but rather connecting to your network, or your Internet Service Provider (ISP). This network has to follow certain rules, and one of those rules is that online requests are replied to by sending the packets of information to your IP address after connection. In general, when you connect to a given wifi network, you will be given an IP address for that computer. However it can change even by just restarting your router. The important aspect to this is that when you simply connect to a wifi network, you can’t guarantee your ip address. This can be sidestepped by masking one’s true IP address through a guaranteed method. There are a few ways this can be accomplished. TOR is a worldwide computer network designed to route traffic through many different servers as a way to hide its user’s origin. By using TOR, it would be very easy to hide your IP address from company sites. However, many companies knowing this will simply block the IP addresses of TOR exit nodes. In addition, scraping through TOR is usually slower than scraping through the general internet because of the multiple routing. Another method is VPN. Virtual private networks provide you with a connection to a separate network that can mask your ip address with the ip address of the VPN server. In addition to providing an IP mask, the information is also encrypted, making it more secure to use. This makes it harder for attackers to eavesdrop on your communications. It is quite simple to get this up and running, but the better ones (ie. the ones that haven’t already been blacklisted by large tech companies) usually cost a monthly subscription fee. For smaller scraping projects that are single scripts running on local setups, it is most efficient to just connect to a VPN service provider."/>



<!-- 	</div>
	<div class="row1"> -->
		<FlipCard date="" subtitle="Distributed Systems Component" msg="Since most websites have anti-web scraping technology, even the best web-scraping programs will time-out before they can finish scraping all the data off a webpage. In addition, libraries like Selenium and Scrapy are not designed to be 100% foolproof--automation is a complicated area of technology so even if you do everything right expect your scraper to just timeout. To protect against this and prevent the dreaded babysitting of code, you can parallelize this procedure by either using multiple threads all running the same script, or by utilizing distributed systems architecture. To do this you would need to create a centralized database that all of your parallel scripts can read and update to ensure they do not duplicate work, and from which you pull the final, completed scraped data from."/>

	<FlipCard date="" subtitle="Machine Learning Component" msg="Sometimes the format of the content you would like to scrape will also present difficulties. As technology advances and cooler, sleeker, more aesthetically pleasing graphics become more normal in websites, there might be information that is stored in a graphic which is not immediately easy to scrape data from. To accomplish this data collection you can use OCR technology, specifically the Tesseract OCR engine. 
	Tesseract OCR is a software library maintained by Google in the python programming language that can scan any image and extract the text and number present in the graphic. It is easy to use and quite powerful--however the tradeoff can be that it is computationally intensive and still does not produce 100% accurate results, so these result may require a final once-over by a human reader. 
	There are other services, for example Google Vision AI which also allows you to extract text and numbers from images, however this service is in a web browser so while it may be easier to use and setup, it is harder to fine-tune and harder to scale."/>




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
