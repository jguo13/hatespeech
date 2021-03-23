<template>
  <div class="about">
<!-- 		<div> <particles-bg type="cobweb" :bg="true" /> </div> -->
	<div class="summarycards">
		<Summarycard image_path="hacker.png" intro_paragraph="Scraping in the U.S. has had a complicated legal history. In general, and especially for large tech companies, scraping data from websites like Facebook or Google will violate their Terms of Service agreements, and thus in that sense is not a strictly legal activity. However, cases have been brought before the courts which have demonstrated that it is possible to get away with scraping--if the context, methods, and reasons are right. The following section details different cases that have challenged the legality of scraping, and the important takeaways of each case."/>

	</div>
	<div class="historycards">

	<div class="row1">
	<FlipCard date="1984" subtitle="Computer Fraud and Abuse Act" msg="The Computer Fraud and Abuse Act, or the CFAA, was enacted by Congress in 1984. In the instances when scraping is prosecuted, it is usually done under the CFAA. When this bill was passed, the World Wide Web had not yet been created, but concerns had started to grow around the crime that computers could enable. It was groundbreaking when enacted because for the first time, it established that hacking, or at least a loosely defined act that has come to be known as “hacking,” was a federal offense. Specifically, the CFAA criminalizes when someone is “exceeding authorized access” (this phrase is often taken to mean violating the terms of service agreement) in order to “obtain information from any protected computer. Most crimes in hacking are punished through the CFAA, but its ambiguous phrasing (most likely ambiguous because the lawmakers themselves were not quite sure how computers would factor into the future of law) has caused issues as prosecutors and defendants take liberties with its interpretation." :links="['https://scholarship.law.uc.edu/cgi/viewcontent.cgi?article=1172&context=uclr','https://www.wired.com/2014/11/hacker-lexicon-computer-fraud-abuse-act/#:~:text=TL%3BDR%3A-,The%20Computer%20Fraud%20and%20Abuse%20Act%2C%20also%20known%20as%20the,from%20its%20digital%20Dark%20Age','https://www.congress.gov/bill/98th-congress/senate-bill/2864']"/>



<!-- 	</div>
	<div class="row1"> -->
		<FlipCard date="2010" subtitle="Auernheimer AT&T Hack" msg="In 2010 Auernheimer and Spitler discovered a vulnerability in the AT&T’s website that would leak the email addresses of people who were using AT&T for 3G wireless network for their iPads. They wrote a script called the “iPad 3G Account Slurper” which would mimic the behavior of iPads contacting the website to collect the emails of these iPad users. Among their collected emails were New York Mayor Michael Bloomberg and then-White house Chief of Staff Rahm Emanuel. The two contacted Gawker to report the security vulnerability, and provided the emails as proof. However AT&T maintained that the duo did not contact the company directly about the vulnerability. A confidential source also supplied the court with private chat logs between the two where they admitted to conducting the harvest to tarnish AT&T’s reputation as well as promote their security company. Auernheimer was convicted and spent 41 months in prison." :links="['hhttps://www.wired.com/2013/03/att-hacker-gets-3-years/','https://www.theverge.com/2013/3/18/4118484/andrew-weev-auernheimer-sentenced-att-ipad-hack']"/>

	<FlipCard date="2019" subtitle="hiQ Labs v. LinkedIn" msg="hiQ is a small data analytics company whose main business is scraping public LinkedIn profiles in order to deliver data on workforce demographics to HR teams. LinkedIn, which had already been bought by Microsoft, filed a cease and desist letter to the company asking them to stop copying data from LinkedIn servers, invoking both the CFAA and the Digital Millennium Copyright Act. On September 9, 2019, the U.S. 9th circuit court of Appeals ruled in favor of hiQ that scraping web sites did not violate the Computer Fraud and Abuse Act. They ruled that forcing hiQ to stop scraping public user profiles would threaten the survival of its business, and that harm outweighed the privacy cost of some LinkedIn users. The panel that ruled this case also added that hiQ raised an important question as to what “without authorization” means in the CFAA, given that hiQ only scraped public LinkedIn user profiles that required no special login or permission to access. This ruling effectively limited the CFAA by stating that hiQ’s case did not fall under it since the data it was accessing was not password protected." :links="['hhttps://globalfreedomofexpression.columbia.edu/cases/hiq-labs-v-linkedin/','https://law.justia.com/cases/federal/appellate-courts/ca9/17-16783/17-16783-2019-09-09.html']"/>


	<FlipCard date="2020" subtitle="Sandvig V. Barr" msg="Sandvig v. Barr is a civil action suit filed by the ACLU and an important case in scraping history because it challenged the constitutionality of the CFAA, arguing that it was a First Amendment Free Speech violation. This was a pre-enforcement challenge, meaning that they were proactively bringing the challenge to the courts rather than wait for themselves to be prosecuted under the CFAA. The plaintiffs were a group of researchers, computer scientists, and journalists from the University of Michigan, the University of Illinois, and Northeastern University. They were scraping employment websites by creating fake user profiles (a violation of the websites’s terms of service agreements) and then using bots to crawl existing user profiles on the websites to gauge the demographics. Their goal was to understand whether employment websites were discriminating against job applicants based on race and gender. The ACLU made the case that the plaintiffs were a group of academic researchers that scraped websites to answer an important question on whether websites were discriminating against protected classes. They were not doing it for money or any material gain, and thus to outlaw scraping was to hinder their important research. On March 30, 2018, the United States District Court of Columbia dismissed the case, ruling that the research done by the plaintiffs would not be considered criminal since it was done on public sites. In addition, the Court observed that if violating the terms of service for any website constituted a criminal activity, then individual website creators would have an improper delegation of legislative authority." :links="['https://www.technologylawdispatch.com/2018/05/big-data/d-c-federal-court-rules-that-web-scraping-does-not-violate-the-cfaa-and-may-be-protected-by-the-first-amendment/#:~:text=On%20March%2030%2C%202018%2C%20a,Sessions%2C%20No','https://www.aclu.org/cases/sandvig-v-barr-challenge-cfaa-prohibition-uncovering-racial-discrimination-online','https://globalfreedomofexpression.columbia.edu/cases/sandvig-v-barr/']"/>

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
