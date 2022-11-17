import streamlit as st
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Data Bakers",
    page_icon=":bird:",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown("<h1 style='text-align: center; color: white;'>Data Bakers</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>Data Scientist, Data Steward, Data Protection Officer, Data Architect... sont les utilisateurs de la data au quotidien</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
col2.image("https://lafactory.ma/wp-content/uploads/2019/11/Data-scientist.jpg")


def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid

mygrid = make_grid(3,3)   
expander00 = mygrid[0][0].expander('Data Analyst')
expander01 = mygrid[0][1].expander('Data scientist')
expander02 = mygrid[0][2].expander('Data Engineer')

expander10 = mygrid[0][0].expander('DataOps')
expander11 = mygrid[0][1].expander('Data Protection Officer')
expander12 = mygrid[0][2].expander('Data Quality Manager')

expander20 = mygrid[0][0].expander('Data Designer')
expander21 = mygrid[0][1].expander('Architecte Big Data')
expander22 = mygrid[0][2].expander('Data Governance Manager')

expander30 = mygrid[0][0].expander('Data Steward ')

with expander00:
    st.markdown("## Fiche métier de data analyst")
    st.image("https://www.michaelpage.fr/sites/michaelpage.fr/files/legacy/shutterstock_1100046194_970x480.jpg")
    st. write("Le data analyst ou analyste de données est responsable de toutes les opérations concernant les bases de données au sein de l'entreprise. Il fait partie de l'équipe de direction des systèmes d'information et doit récolter toutes les données fournies par les clients afin de les intégrer dans la base de données de l'entreprise.")
    st.markdown("### Data analyst : fonctions et responsabilités")
    st.markdown("""
    Le data analyst doit retranscrire une problématique marketing et business en statistiques. Il doit donc trouver des sources et des chiffres pertinents, mais contrairement au data scientist, qui a une vision globale de la stratégie, le data analyst se concentre uniquement sur une seule source de données. Ses principales fonctions et responsabilités sont :
    - le recueil et l'extraction de sources de données qui seront ensuite traduites en statistiques
    - l'analyse des données recueillies et leur tri en fonction de leur pertinence pour la problématique de l'entreprise
    - la gestion et le stockage des données grâce à la mise en place de solutions 
    - la confection et la maintenance d'un entrepôt de données (data warehouse) permettant de conserver et d'utiliser régulièrement les données
    - la synthétisation et la vulgarisation des données afin de les rendre accessibles aux dirigeants de l'entreprise ainsi qu'aux autres services concernés
    - l'amélioration constante du système de récupération des données client afin d'optimiser et d'agrandir le stock de données possédé par l'entreprise
    - la connaissance des évolutions technologiques pour que l'entreprise ne prenne jamais de retard sur la concurrence.
    """)


with expander01:
    st.markdown("## Fiche métier de data scientist")
    st.image("https://pbs.twimg.com/media/ElAa8e-W0AAei05.jpg")
    st. write("Le data scientist ou analyste de données est un spécialiste des statistiques au service du département marketing. Il collecte les données des clients et les traite pour obtenir une connaissance plus précise de leur profil, afin que l'entreprise puisse ensuite proposer des produits ou services au rendement optimal.")
    st.markdown("### Data scientist : fonctions et responsabilités")
    st.markdown(""" Le data scientist occupe un rôle-clé dans le département marketing de l'entreprise, car il établit une stratégie permettant de récupérer des données hétérogènes indispensables au développement d'un projet. Il peut aussi exercer dans d'autres domaines de l'entreprise grâce à ses solutions statistiques. Ses principales fonctions sont :
    - la collecte, la sélection et le traitement de données appartenant au client et qui ont un intérêt pour la stratégie marketing de l'entreprise ;
    - la prise en compte de la problématique générale de l'entreprise dans tous les domaines (marketing, finance, commercial, etc.), afin de concevoir la solution la plus optimale pour le stockage des données ;
    - la gestion et le stockage des données, grâce à la mise en place de solutions ;
    - la conception d'outils permettant l'élaboration d'un entrepôt de données (data warehouse) ;
    - la maîtrise et la protection des flux de données ;
    - l'élaboration de scénarios que l'entreprise pourrait rencontrer, afin de proposer des solutions d'anticipation ;
    - l'amélioration constante du système de récupération des données client, afin d'optimiser et d'agrandir le stock de données de l'entreprise.
    """)


with expander02:
    st.markdown("## Le métier de Data Engineer")
    st.image("https://cdn.futura-sciences.com/sources/images/data_engineer1.jpg")
    st.markdown("""
    Le Data Engineer évolue dans le domaine des sciences de données. Il est chargé de trouver la solution pour importer un très grand nombre de données. Il rend plus facile leur collecte, leur analyse et leur stockage.Le Data Engineer est le responsable de l'infrastructure analytique de l'ensemble des données d'une entreprise. Son travail permet à l'équipe de Data Scientist d'analyser les données collectées.
    """)
    st.markdown("### Les missions du poste de Data Engineer")
    st.markdown(""" Le Data Engineer met en place et rend opérationnel l'architecture et les infrastructures Big Data d'un client.
    Il conçoit donc des solutions qui permettent le traitement d'un volume très important de données.
    Le Data Engineer développe le flux de données et les prépare pour leur analyse. Il travaille en amont des Data Scientist.Son travail consiste à programmer, automatiser et optimiser les algorithmes de l'infrastructure ce qui permet ensuite aux équipes de Data Analyst et Data Scientist d'analyser les données collectées. Il intervient aussi auprès d'une équipe de Data tout au long des étapes de traitement des données.Tout au long de l'avancement du projet, il veille de manière permanente au maintien des technologies, langages et du bon fonctionnement des infrastructures. Il doit avoir une connaissance pointue des langages comme Javascript, Python, Scala.
    """)
    st.markdown("### Les compétences techniques")
    st.markdown("""
    - Maitrise des langages : Python, C / C ++, Java, Perl UNIX, Linux et Solaris.
    - Maîtrise de divers systèmes d'exploitation : UNIX, Linux, Solaris...
    - Connaissances en solutions de bases de données : SQL, NoSQL.
    - Connaissance générale en terme de Big Data.
    - Maitrise de ses technologies Anglais.
    """)


    st.markdown("### Softskills nécessaires pour le poste")
    st.markdown("""
    - Mobilité
    - Disponibilité
    - Esprit d'analyse
    - Capacité d'organisation et d'analyse
    - Adaptation
    - Relationnel
    - Force de proposition
    - Réactivité
    - Rigueur
    """)





st.markdown("___")


with expander10:
    st.markdown("## Fiche métier de DataOps")
    st.image("https://www.decideo.fr/photo/art/grande/43370848-35813186.jpg?v=1583399550")
    st. markdown("#### le DevOps appliqué à la data")
    st.write("Avec l'essor de l'apprentissage automatisé (Machine Learning ou ML) et de l'intelligence artificielle (IA), les données sont générées en masse. Collectées ensuite par les entreprises, elles ne sont pas toujours maîtrisées. La démarche DataOps vise à gérer ces données avec efficience. Des plateformes et des outils dédiés permettent de mettre en œuvre cette méthodologie. Les pratiques associées sont au cœur du métier de l'ingénieur DataOps.")
    st.markdown("### Le DataOps, qu'est-ce que c'est ?")
    st.markdown("""
        Le DataOps (Data Operations) optimise le cycle de vie des projets Data (relatifs aux données) et des analyses qui en sont issues. Selon le Gartner, il s'agit d'une pratique de gestion des données collaborative qui a pour but de favoriser l'exploitation de l'analytique dans les entreprises.
    """)
    st.markdown("### Quels sont les bénéfices du DataOps ?")
    st.markdown("""
        Le DataOps tend à accroître la rapidité et l'efficacité dans le traitement des données, afin qu'elles soient analysables et exploitables par les entreprises. Une meilleure productivité des équipes informatiques et une réduction des risques commerciaux constituent les principaux atouts de cette méthodologie.
    """)

    st.markdown("### Que recommande le DataOps Manifesto for agile ?")
    st.markdown("""
        Ce document référent en matière de méthodologie DataOps liste au total 18 principes. Ceux-ci comprennent notamment : la satisfaction continue du client, la valorisation des analyses de travail, l'acceptation du changement, la pluralité des rôles et des compétences dans les équipes (une diversité d'opinions encourageant l'innovation et la productivité), l'auto-organisation…

        Le manifeste reprend les principales caractéristiques de la méthode agile, appliquées plus spécifiquement à l'approche du DataOps.
    """)

    st.markdown("### Quels sont les principaux outils et plateformes de DataOps ?")
    st.markdown("""
        Des éditeurs proposent des outils et des plateformes qui supportent cette méthodologie afin de faciliter sa mise en œuvre au sein des équipes. Ces solutions ont pour principal objectif la gestion du cycle de vie d'un projet Data, de sa création à sa mise en production. Saagie, IBM et Datalytyx, par exemple, ont créé des solutions complètes pour intégrer ces pratiques.
    """)


    st.markdown("### DataOps ingénieur : quel profil de compétences, salaire et formation ?")
    st.markdown("""
        L'ingénieur DataOps doit avoir un bac + 5 en informatique orientée Big Data (cursus universitaire en plein développement), ou être titulaire d'un diplôme d'ingénieur spécialisé dans la Data. Il pilote le pipeline d'analyse de données en production, et vérifie la disponibilité et la performance des systèmes. Selon sa formation et son expérience, le salaire d'un ingénieur DataOps oscille entre 50 et 80 KE par an.
    """)

    st.markdown("### DataOps vs DevOps")
    st.markdown("""
        Le DataOps intègre la base de données dans les tests, il s'agit de DevOps appliqué aux données afin de répondre à un besoin plus précis. Les deux démarches sont collaboratives et impliquent plusieurs métiers, le DataOps étant spécifiquement orienté vers les entreprises tournées vers la Data.
    """)

    st.markdown("### DataOps vs MLOps")
    st.markdown("""
        D'un point de vue méthodologique, on retrouve les mêmes approches adaptées à des domaines différents, bien que liés. Le DataOps participe au déploiement, à l'analyse et au monitoring des données (Data), tandis que le MLOps est orienté vers la création, le déploiement et le monitoring des modèles d'apprentissage automatique (Machine Learning).
    """)


    

with expander11:
    st.markdown(""" ## Fiche métier de Data Protection Officer """)
    st.image("https://www.michaelpage.fr/sites/michaelpage.fr/files/styles/advice_node_desktop/public/legacy/DPO.jpg?itok=_8GhdP_r")
    st.markdown("""

    Fonction récente pour l'entreprise, le DPO a pour responsabilité de garantir la conformité des mécanismes de traitement et de stockage des données de son organisation, qu'elles soient à usage commercial ou interne, notamment dans le domaine RH.")
    ### Responsabilités du Data Protection Officer")

    - Cartographier les catégories de données à sécuriser pour répondre aux exigences réglementaires et techniques de la législation en cours
    - Conseiller et contrôler l'ensemble des métiers concernés par la protection des données
    - Mener une veille technologique et réglementaire permanente
    - Sensibiliser, former et contrôler l'intervention des collaborateurs concernant la manipulation d'informations dites « sensibles » aux yeux de la loi
    - Être un intermédiaire avec la CNIL dans le cadre de la mise en conformité et des audits.
    
    ### Rattachement du DPO
    Le Data Protection Officer est souvent rattaché à la Direction Juridique ou directement au Directeur des Systèmes d'Information ou au Directeur de la Sécurité des SI. 

    ### Profil et formation du Data Protection Officer 
    Le Data Protection Officer dispose de solides compétences autour de la sécurité des SI et notamment de la cyber sécurité. Il est parfois issu de ces filières, parfois du juridique avec néanmoins une culture poussée des contraintes et solutions technologiques à mettre en œuvre pour sécuriser le traitement de ses données.

    Sa formation initiale est en général un bac + 5 ingénieur ou son équivalent universitaire dans la filière juridique. 

    Il possède au moins 5 ans d'expérience dans le domaine de la sécurité des systèmes d'information souvent complétés par une expérience plus « réglementaire » sur le sujet.

    """)


with expander12:
    st.markdown(""" ## Fiche métier de Data Quality Manager """)
    st.image("https://www.datagalaxy.com/wp-content/uploads/2021/03/B-Datqualaity-quel-role_-1.png")
    st.markdown("""

    Le Data Quality Manager est responsable de la gestion de la qualité des données de l'entreprise. Mais quel est son rôle et quelles sont ses missions ? Zoom sur ce métier de Data Bakers !

    ### Qu'est-ce qu'un Data Quality Manager ?
    Le Data Quality Manager est chargé de vérifier que les données collectées, stockées et utilisées par tous les métiers de l'entreprise sont correctes et à jour. Il doit également assurer la standardisation de la data : par exemple, créer une structure commune pour référencer tous les produits de l'entreprise. Il est plus simple de retrouver les informations recherchées si les bases de données sont bien organisées !

    Rôle transversal, le Data Quality Manager travaille avec d'autres Data Bakers, mais aussi d'autres métiers en général. Il doit comprendre le fonctionnement et les besoins métiers de tous les collaborateurs de l'entreprise pour adapter l'organisation des bases de données.

    ##### Garant de la qualité des données

    Pour garantir la data quality de l'entreprise, il doit analyser les données et identifier celles qui ne sont pas qualifiées (fausses, incomplètes, doubles…). Lorsqu'il trouve une donnée erronée, il doit identifier sa source et comprendre l'origine du problème. Il peut ensuite mettre en place les chantiers nécessaires et conseiller les métiers sur les conditions d'utilisation des données.

    Il peut être assigné à un champ d'activité particulier, comme les données liées au marketing et à la vente. De plus en plus d'entreprises utilisent un CRM : à l'aide du Data Quality Manager, les données stockées et utilisées sont standardisées mais aussi enrichies.

    ### Le rôle du Data Quality Manager

    Le Data Quality Manager doit s'assurer que les données sont correctes et régulièrement mises à jour : une donnée obsolète peut avoir des conséquences négatives sur l'ensemble des informations. 

    Si les décideurs n'ont pas les bonnes informations sur leurs clients, par exemple, ils risquent de prendre des décisions inadaptées à la situation. Le Quality Manager a donc le devoir de garantir une data propre, actualisée et utilisable par tous les métiers de l'entreprise. Essentiel pour éviter les mauvaises surprises !

    Le Data Quality Manager vérifie également qu'il n'y a pas de doublon entre les différentes sources et bases de données pour que la data soit bien standardisée. Une base propre est utile à tous les niveaux de l'entreprise : les métiers peuvent s'appuyer sur la data pour prendre des décisions, il y a un réel gain de place de stockage et, par conséquent, les coûts sont réduits.

    ### Les missions principales du Data Quality Manager

    Ses missions sont diverses et variées, il doit assurer :

    - la mise en place des standards de qualité de la donnée de l'entreprise ;
    - le respect des standards par l'ensemble de l'entreprise ;
    - des propositions de changements dans les processus d'utilisation de la donnée ou les systèmes informatiques ;
    - le reporting sur la performance et la qualité de la donnée ;
    - l'évangélisation de l'importance de la data quality auprès des métiers et l'explication des bonnes pratiques.   

    ### Quelles sont les compétences et les qualités requises ?
    Pour être efficace, le Data Quality Manager doit avoir de solides connaissances en data et en Business Intelligence. Il doit également être capable de faire des analyses poussées, mais aussi de repérer les problèmes rencontrés et de proposer des solutions.

    Puisqu'il collabore avec de nombreux métiers de la data, il est amené à gérer des projets et à animer des équipes : une bonne aisance relationnelle est donc requise. 
    
    ### À ne pas confondre avec…

    Le Data Quality Manager ne doit pas être confondu avec le rôle du Data Engineer. Ce dernier garantit l'exploitation technique des données et leur sécurité. Il travaille également sur l'infrastructure des technologies déployées par l'entreprise. Le Data Quality Manager, quant à lui, établit les processus et les pratiques nécessaires pour assurer des données de qualité : actualisées, standardisées et sans doublon !

    Vous voulez en savoir plus sur les métiers de la Data ? Découvrez dès maintenant le Data Engineer. 
    """)


with expander20:
    st.markdown(""" ## Comment devenir data designer ? """)
    st.image("https://www.seacom.it/wp-content/uploads/2020/05/data-viz.jpeg")
    st.markdown("""
    L'univers du digital a donné naissance à plusieurs nouveaux emplois. Il ne se limite plus à des activités sommaires allant de l'agencement d'un système à la réparation des outils physiques. Le numérique est devenu plus riche de sens : des données que le data designer va mettre en exergue grâce au data design.

    ### Les missions d'un data designer

    Comme son nom l'indique, un data designer se charge de mettre en avant de manière artistique et visuelle, la présentation des data — les données. En d'autres termes, il travaille uniquement sur les données fournies par un client ou un intervenant, et veille à les représenter sous une forme compréhensible par un public donné. Il peut s'agir de graphes, de camemberts, de courbes ou de toutes autres représentations visuelles.

    Dans le data design, l'expert a cependant plus d'options et de liberté dans l'animation (ou non) de sa présentation. Toutefois, la conception doit avant tout se baser sur la mise en avant des données essentielles. Le métier de data designer se base essentiellement sur la data. C'est ce qui fait toute la différence de cette profession avec le métier d'un infographiste ou toutes personnes travaillant dans l'univers du graphisme.

    Dans le data design, ou le design des données, l'expert doit collaborer étroitement avec le client ou l'intervenant, c'est-à-dire le propriétaire des données qui a besoin d'illustrer ses data sous une autre forme. Cette méthode de travail permet de mieux appréhender l'agencement du produit final. Le client doit fournir les directives nécessaires pour délimiter les données essentielles à mettre en valeur.
    Le data designer se charge par la suite de proposer des illustrations. Celles-ci doivent être validées par le principal concerné et discutées entre les deux parties. En d'autres termes, tout le savoir-faire d'un data designer est concentré sur les données de sorte à pouvoir offrir une bonne visualisation de ces dernières. Le but est qu'elles puissent être comprises dans les ouvrages ou lors des conférences.


    ### Les compétences d'un data designer
    Afin d'exercer en tant que data designer, une base en infographie est indispensable pour maîtriser le concept de « design ». Il faut également posséder un grand sens de l'analyse pour définir le type de data à mettre en exergue et la manière de procéder pour obtenir un résultat concret. Posséder le sens de la communication est également un atout majeur dans l'univers du digital. Le data designer n'échappe pas à la nécessité d'échanger avec ses pairs, mais surtout avec le demandeur de service (ou le client) dans la mesure où ce dernier joue un rôle considérable dans la réalisation des illustrations.

    ### Les formations accessibles
    Il existe plusieurs formations pour devenir un data designer. Dispensées par des écoles spécialisées, elles ne sont pas uniquement centrées sur le data design, mais s'ouvrent aussi sur d'autres champs à l'image de l'infographie, du design d'interface, du design multimédia et bien plus encore.    
        """)
    

with expander21:
    st.markdown(""" ## Fiche métier de Architecte Big Data """)
    st.image("https://actualiteinformatique.fr/wp-content/uploads/2020/03/Metier-Data-Architect.png")

    st.markdown("""
    ### Rôle et missions de l'architecte Big Data
    C'est la personne qui se charge de collecter des données brutes pour l'entreprise. Les données en question peuvent provenir d'une multitude de sources internes ou externes, et peuvent être structurées ou non. Leur quantité peut aussi varier énormément. Il doit mettre en place l'infrastructure qui permettra de stocker, d'ingérer les données dans les applications métiers.

    Après avoir collecté les données brutes, l'architecte Big Data se charge de créer et d'optimiser des infrastructures de stockage, manipulation et restitution. Il doit élaborer une architecture de Data Management et concevoir un plan pour intégrer, centraliser, protéger et maintenir les données. Il est garant du bon fonctionnement du système qui doit pouvoir s'étendre selon les besoins du clients.

    ### Architecte Big Data : compétences et qualités nécessaires
    Il doit impérativement maîtriser les technologies Big Data. Parmi les outils qu'il doit savoir utiliser, on compte les bases de données NoSQL comme MongoDB, Cassandra ou Redis. Il est aussi nécessaire de manier les infrastructures serveur comme Hadoop et Spark. Enfin, les outils de stockage de données en mémoire comme Memtables doivent aussi faire partie de son arsenal.

    Ce professionnel travaille au quotidien avec les Data Scientists de son entreprise. Il se charge notamment de leur fournir les données brutes que ces derniers devront traiter et analyser. Il doit donc être doté d'un solide esprit d'équipe et de collaboration, et de compétences en communication.
    
    ### Architecte Big Data : diplômes et formations

    Pour accéder au poste d'architecte Big Data, un diplôme de niveau Bac+4 ou Bac+5 est nécessaire. Il est possible de miser sur une formation en informatique, management, statistiques ou marketing. Précisons toutefois que la plupart des architectes Big Data sont des profils seniors dotés d'une longue expérience dans le domaine de la Business Intelligence. C'est dans cette branche qu'ils auront appris à déployer des installations qui doivent supporter une charge forte tout en restant rapide.

    Exemples de formations :
    - Master european master in datamining and knowledge management (Lyon 2)
    - Master statistiques pour l'évaluation et la prospective (université de Reims-Champagne Ardennes)
    - Master MIASHS : big data et fouille de données (Paris 8)
    - Master Data Science (Grenoble INP Ensimag, Polytech Nantes)
    - Mastère en ingénierie Big data (ESGI)
    - MSc statistics for smart data (Ensai)
    - MSc big data for business (Ecole polytechnique – HEC)
    - MSc data sciences & business analytics (Centrale Supelec – Essec Business School)
    - MSc applied data science & big data (Data science institute)
    - MSc data science (Ensae ParisTech)
    - MSc data management (PSB)
    - IAMD – ingénierie et applications des masses de données (Télécom Nancy)
    - Big Data & data science (Mines Nancy)
    - Data Science (Ensae ParisTECH)
    - Ingénierie des systèmes d'information (Grenoble INP Ensimag)
    - MS Big data – gestion et analyse des données massives (Télécom ParisTech)
    - MS Big data : analyse management et valorisation responsable (Ensimag + EMSI École de management de Grenoble)
    
    ### Architecte Big Data : insertion sur le marché professionnel

    C'est l'un des profils les plus recherchés parmi les différents métiers du Big Data. De fait, ce professionnel qualifié trouvera facilement du travail dans les entreprises de toute envergure et dans toutes les industries. Les grandes entreprises sont à privilégier, car ces dernières ont impérativement besoin d'un architecte Big Data et sont prêtes à y mettre le prix.

    Au fil des années, l'architecte Big Data évolue et se voit confier la gestion de projets plus importants, plus volumineux ou plus complexes. Il s'agit donc d'un poste à responsabilités.

    ### Missions
    - Collecter des données brutes pour l'entreprise
    - Créer des infrastructures de stockage, manipulation et restitution
    - Elaborer une architecture de Data Management
    
    ### Compétences
    - Maîtrise des technologies Big Data
    - Maîtrise des infrastructures serveur
    - Esprit de collaboration
    - Talent de communication
    
    ### Diplômes et formations
    - Bac+4 ou 5 en informatique, management, statistiques ou marketing
    - Formation Big Data
    - Ecole d'ingénieur spécialisée
    - Expérience professionnelle Business Intelligence
    """)

with expander22:
    st.markdown("""
    ## Fiche métier de Data Governance Manager """)
    st.image("https://www.redsen-consulting.com/wp-content/uploads/DM_DataGovernance.jpg")
    st.markdown("""
    Le Data Governance Manager est le responsable de la stratégie de gouvernance des données dans l'entreprise. Il dirige et gère toutes les activités de gouvernance à l'échelle de l'organisation, étant aussi responsable de l'amélioration de la qualité des données et de la protection des actifs de données.

    En tant que Data Governance Manager, le responsable aura pour principale mission d'établir et assurer le respect d'un cadre de gouvernance des données d'entreprise, avec la mise en place de normes et bonnes pratiques relatives aux données circulant dans l'entreprise. Ces normes fonctionnelles apporteront une cohérence de qualité et de protection des données.

    En travaillant en étroite collaboration avec les responsables des différents départements de l'entreprise, il assure un niveau d'exigence pour la qualité des données collectées, en améliorant la protection réglementaire et en soutenant une stratégie de gouvernance adaptée.

    ### Pourquoi le Data Governance Manager est important ?
    Le Data Governance Manager est un collaborateur important de part son poste stratégique. Plus personne ne doute aujourd'hui de l'importance de mettre en place une stratégie de gouvernance des données efficace et réfléchie. L'importance et la variété des missions du Data Governance Manager dépendront de la structure qu'il intègre, que ce soit par rapport à sa taille ou son fonctionnement.

    ### Quels sont les bénéfices à attendre grâce au Data Governance Manager ?
    Les bénéfices apportés par un Data Governance Manager sont nombreux. C'est lui qui établit et gère une feuille de route pour la mise en oeuvre de la gouvernance des données d'entreprise, y compris l'établissement des priorités stratégiques liées aux données. En déployant un cadre de gouvernance des données à l'échelle de l'entreprise, axé sur l'amélioration de leur qualité et leur protection, il permet une confiance renforcée dans ces dernières.

    Ensuite, c'est aussi à lui de définir les rôles et responsabilités liés à la gouvernance des données et assurer un degré de responsabilité clair aux Data Steward. Il assure une liaison entre les secteurs fonctionnels et techniques afin de s'assurer que les exigences liées à la protection des données sensibles soient prises en compte dans la planification des objectifs de chacun.

    ### Quelle sont les compétences à avoir pour devenir un Data Governance Manager ?
    Le Data Governance Manager doit posséder différentes compétences directement liées à son rôle stratégique dans l'entreprise. Il doit notamment pouvoir facilement diriger des équipes, articuler une vision de transformation et une volonté de changement qui l'amèneront à donner une direction claire à l'entreprise.

    Ensuite, le Data Governance Manager devra pouvoir superviser des projets. Il pourra être capable de décomposer des problèmes et des projets complexes en objectifs gérables.    

    """)


with expander30:
    st.markdown("""
    ## Fiche métier de Data Steward  """)
    st.image("https://www.blueway.fr/wp-content/uploads/2021/01/Data-steward.jpg")
    st.markdown("""
    Le Data Steward coordonne la donnée. C'est le gouvernant de la donnée qui l'organise et la gère. Il s'assure également de la qualité de la data dans une l'organisation.

    ### QU'EST-CE QU'UN DATA STEWARD ?
    Le Data Steward est un autre métier issu de la famille de la Data. Les entreprises utilisent de plus en plus la Data et créent de nouveaux postes afin de répondre aux enjeux qui y sont associés. Le Data Engineer conçoit les pipelines de données, le Data Analyst les analysent et le Data Scientist conçoit et applique des algorithmes, le Data Steward a lui une tâche toute aussi importante. Ce dernier est le responsable de la qualité de la donnée. C'est donc à lui de vérifier les lacs de données ou datalakes et s'assurer que ceux-ci sont parfaits. En cela, c'est un maillon extrêmement important de la chaîne de la donnée.

    Pour nettoyer les datalakes, le Data Steward veillera à plusieurs points importants, comme la bonne définition de la donnée en identifiant les possibles conflits dans la donnée, la non présence de doublons ainsi que la fraîcheur des données qui seront analysées en supprimant le contenu obsolète. Il devra également créer des procédés respectés par tous les acteurs de la donnée dans l'entreprise par le biais d'une politique interne de standardisation. Son but est également de veiller à la qualité de la donnée en procédant à des corrections régulières basées sur les retours de l'équipe Data. Outre ses missions, il joue également un rôle important dans la communication entre les différentes équipes.

    C'est le “maître” de la data, ses compétences dans les différents logiciels ainsi que sa mission de gouvernance de la Data lui oblige d'être particulièrement minutieux sur la sécurité de la donnée.


    ### MISSIONS DU DATA STEWARD
    - Assurer la qualité de la sécurité des données,
    - Garantir la gestion et la qualité de la data,
    - Veiller au respect des politiques et normes tout en partageant les bonnes pratiques avec les différentes équipes.

    ### PROFIL DU DATA STEWARD
    Il sort d'une formation supérieure en école d'ingénieur, école d'informatique ou Master spécialisé dans la Data Science ou Intelligence Artificielle. Une première expérience acquise en stage ou en alternance est fortement requise pour obtenir les compétences requises à ce métier.
    
    ### COMPÉTENCES DU COORDONNATEUR DE DONNÉES

    - Maîtrise des technologies du Big Data permettant le traitement et la manipulation de données,
    - Connaissances en solutions de bases de données (SQL, NoSQL…),
    - Forte expertise le stockage de données et les outils ETL,
    - Maîtrise des langages structurés (Javascript, Scala, Python…),
    - Anglais courant,
    - Connaissance des méthodologies agiles.

    ### QUALITÉS DU COORDONNATEUR DE DONNÉES
    - Force de proposition,
    - Rigueur,
    - Réactivité,
    - Esprit analytique et de synthèse,
    - Esprit d'équipe,
    - Excellent relationnel,
    - Sens de l'organisation,
    - Sens de la qualité.

    ### ÉVOLUTION DE CARRIÈRE DU DATA STEWARD
    Une évolution vers d'autres métiers de la Data est envisageable pour quelqu'un qui souhaite continuer dans ce cœur de métier mais en opérant sur des étapes différentes du traitement de la donnée. Un Data Steward peut envisager de devenir Data Scientist, Data Engineer, Chief Data Officer…
    """)




# dataset
data = {'data analyst':42000 , 'data scientist':42160 , 'Data Engineer':42780,
        'DataOps':43000, 'Data Protection Officer':48000, 'Data Quality Manager':53178,
        'data designer':20520, 'Architecte Big Data':61822, 'Data Governance Manager':124800,
        'Data Steward':42078}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 3))
 
# creating the bar plot
plt.bar(courses, values, color ='maroon',
        width = 0.4)

plt.xlabel("métier")
plt.xticks(rotation=60, ha='right')
plt.ylabel("Salaire brut/an en €")
plt.title("les salaires moyens  de Data Bakers en France (brut/an)")
st.pyplot(fig)
