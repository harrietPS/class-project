from bs4 import BeautifulSoup
import requests, json

plant_data = json.dumps({
	"Malaxis unifolia Michx.": {
		"wikidata": "Q6741526",
		"Plantlist": "kew-118674",
		"Tropicos": "23503042",
		"GoBotany": "https://gobotany.newenglandwild.org/species/malaxis/unifolia/"
	},
	"Dryopteris campyloptera Clarkson": {
		"wikidata": "Q5309777",
		"Plantlist": "",
		"Tropicos": "26600143",
		"GoBotany": "https://gobotany.newenglandwild.org/species/dryopteris/campyloptera/"
	},
	"Cypripedium reginae Walter": {
		"wikidata": "Q977605",
		"Plantlist": "kew-54339",
		"Tropicos": "23500652",
		"GoBotany": "https://gobotany.newenglandwild.org/species/cypripedium/reginae/"
	},
	"Crassula aquatica (L.) Schoenl": {
		"wikidata": "Q159424",
		"Plantlist": "kew-2741500",
		"Tropicos": "8901390",
		"GoBotany": "https://gobotany.newenglandwild.org/species/crassula/aquatica/"
	},
	"Scleria pauciflora Muhl. ex Willd. var. caroliniana (Willd.) Alph. Wood": {
		"wikidata": "Q24692192",
		"Plantlist": "kew-265592",
		"Tropicos": "9902053",
		"GoBotany": "https://gobotany.newenglandwild.org/species/scleria/pauciflora/"
	},
	"Onosmodium virginianum (L.) A. DC.": {
		"wikidata": "Q15594827",
		"Plantlist": "",
		"Tropicos": "4001026",
		"GoBotany": "https://gobotany.newenglandwild.org/species/onosmodium/virginianum/"
	},
	"Isotria medeoloides (Pursh) Raf.": {
		"wikidata": "Q6086561",
		"Plantlist": "kew-103160",
		"Tropicos": "23502999",
		"GoBotany": "https://gobotany.newenglandwild.org/species/isotria/medeoloides/"
	},
	"Liparis liliifolia (L.) Rich. ex Ker Gawl.": {
		"wikidata": "Q15492395",
		"Plantlist": "kew-112958",
		"Tropicos": "23503019",
		"GoBotany": "https://gobotany.newenglandwild.org/species/liparis/liliifolia/"
	},
	"Cacalia suaveolens L.": {
		"wikidata": "Q21872129",
		"Plantlist": "",
		"Tropicos": "2744893",
		"GoBotany": "https://gobotany.newenglandwild.org/species/senecio/suaveolens/"
	},
	"Asclepias variegata L.": {
		"wikidata": "Q13389383",
		"Plantlist": "kew-2655268",
		"Tropicos": "2603862",
		"GoBotany": "https://gobotany.newenglandwild.org/species/asclepias/variegata/"
	},
	"Aster radula Aiton": {
		"wikidata": "Q5413959",
		"Plantlist": "gcc-89580",
		"Tropicos": "50008740",
		"GoBotany": "https://gobotany.newenglandwild.org/species/eurybia/radula/"
	},
	"Cheilanthes lanosa (Michx.) D.C. Eaton": {
		"wikidata": "Q15611266",
		"Plantlist": "",
		"Tropicos": "tro-26602738",
		"GoBotany": "https://gobotany.newenglandwild.org/species/cheilanthes/lanosa/"
	},
	"Eupatorium aromaticum L.": {
		"wikidata": "Q21874227",
		"Plantlist": "",
		"Tropicos": "2713515",
		"GoBotany": "https://gobotany.newenglandwild.org/species/ageratina/aromatica/"
	},
	"Angelica lucida L.": {
		"wikidata": "Q4762689",
		"Plantlist": "kew-2639149",
		"Tropicos": "1700811",
		"GoBotany": "https://gobotany.newenglandwild.org/species/angelica/lucida/"
	},
	"Ligusticum scoticum L.": {
		"wikidata": "Q3257294",
		"Plantlist": "kew-2343883",
		"Tropicos": "1700838",
		"GoBotany": "https://gobotany.newenglandwild.org/species/ligusticum/scoticum/"
	},
	"Platanthera blephariglottis (Willd.) Lindl.": {
		"wikidata": "Q7202171",
		"Plantlist": "kew-157049",
		"Tropicos": "23503068",
		"GoBotany": "https://gobotany.newenglandwild.org/species/platanthera/blephariglottis/"
	},
	"Bouteloua curtipendula (Michx.) Torr.": {
		"wikidata": "Q4950436",
		"Plantlist": "kew-399418",
		"Tropicos": "25510763",
		"GoBotany": "https://gobotany.newenglandwild.org/species/bouteloua/curtipendula/"
	},
	"Lachnanthes caroliana (Lam.) Dandy": {
		"wikidata": "Q6468494",
		"Plantlist": "kew-251506",
		"Tropicos": "14900001",
		"GoBotany": "https://gobotany.newenglandwild.org/species/lachnanthes/caroliniana/"
	},
	"Castilleja coccinea (L.) Spreng.": {
		"wikidata": "Q5049899",
		"Plantlist": "kew-2704941",
		"Tropicos": "",
		"GoBotany": "https://gobotany.newenglandwild.org/species/castilleja/coccinea/"
	},
	"Cryptogramma stelleri (S.G. Gmel.) Prantl": {
		"wikidata": "Q15235838",
		"Plantlist": "",
		"Tropicos": "26600105",
		"GoBotany": "https://gobotany.newenglandwild.org/species/cryptogramma/stelleri/"
	},
	"Diplazium pycnocarpon (Spreng.) Broun": {
		"wikidata": "Q5279807",
		"Plantlist": "",
		"Tropicos": "26605151",
		"GoBotany": "https://gobotany.newenglandwild.org/species/diplazium/pycnocarpon/"
	},
	"Carex barrattii Schwein. & Torr.": {
		"wikidata": "Q5039084",
		"Plantlist": "kew-224878",
		"Tropicos": "9904370",
		"GoBotany": "https://gobotany.newenglandwild.org/species/carex/barrattii/"
	},
	"Scutellaria integrifolia L.": {
		"wikidata": "Q15364990",
		"Plantlist": "kew-189233",
		"Tropicos": "17601777",
		"GoBotany": "https://gobotany.newenglandwild.org/species/scutellaria/integrifolia/"
	},
	"Pycnanthemum clinopodioides Torr. & A. Gray": {
		"wikidata": "Q3411171",
		"Plantlist": "kew-171039",
		"Tropicos": "17601660",
		"GoBotany": ""
	}
})
