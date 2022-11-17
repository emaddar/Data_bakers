import streamlit as st

st.set_page_config(
    page_title="Data Bakers",
    page_icon=":bird:",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown("# Data Bakers")
st.subheader("Data Scientist, Data Steward, Data Protection Officer, Data Architect... sont les utilisateurs de la data au quotidien")


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
expander11 = mygrid[0][1].expander('Data scientist')
expander12 = mygrid[0][2].expander('Data Engineer')

with expander00:
    st.markdown("## Fiche métier de data analyst")
    st. write("Le data analyst ou analyste de données est responsable de toutes les opérations concernant les bases de données au sein de l’entreprise. Il fait partie de l’équipe de direction des systèmes d’information et doit récolter toutes les données fournies par les clients afin de les intégrer dans la base de données de l’entreprise.")
    st.markdown("### Data analyst : fonctions et responsabilités")
    st.markdown("""
    Le data analyst doit retranscrire une problématique marketing et business en statistiques. Il doit donc trouver des sources et des chiffres pertinents, mais contrairement au data scientist, qui a une vision globale de la stratégie, le data analyst se concentre uniquement sur une seule source de données. Ses principales fonctions et responsabilités sont :
    - le recueil et l’extraction de sources de données qui seront ensuite traduites en statistiques
    - l’analyse des données recueillies et leur tri en fonction de leur pertinence pour la problématique de l’entreprise
    - la gestion et le stockage des données grâce à la mise en place de solutions 
    - la confection et la maintenance d’un entrepôt de données (data warehouse) permettant de conserver et d’utiliser régulièrement les données
    - la synthétisation et la vulgarisation des données afin de les rendre accessibles aux dirigeants de l’entreprise ainsi qu’aux autres services concernés
    - l’amélioration constante du système de récupération des données client afin d’optimiser et d’agrandir le stock de données possédé par l’entreprise
    - la connaissance des évolutions technologiques pour que l’entreprise ne prenne jamais de retard sur la concurrence.
    """)


with expander01:
    st.markdown("## Fiche métier de data scientist")
    st. write("Le data scientist ou analyste de données est un spécialiste des statistiques au service du département marketing. Il collecte les données des clients et les traite pour obtenir une connaissance plus précise de leur profil, afin que l’entreprise puisse ensuite proposer des produits ou services au rendement optimal.")
    st.markdown("### Data scientist : fonctions et responsabilités")
    st.markdown(""" Le data scientist occupe un rôle-clé dans le département marketing de l’entreprise, car il établit une stratégie permettant de récupérer des données hétérogènes indispensables au développement d’un projet. Il peut aussi exercer dans d’autres domaines de l’entreprise grâce à ses solutions statistiques. Ses principales fonctions sont :
    - la collecte, la sélection et le traitement de données appartenant au client et qui ont un intérêt pour la stratégie marketing de l’entreprise ;
    - la prise en compte de la problématique générale de l’entreprise dans tous les domaines (marketing, finance, commercial, etc.), afin de concevoir la solution la plus optimale pour le stockage des données ;
    - la gestion et le stockage des données, grâce à la mise en place de solutions ;
    - la conception d’outils permettant l’élaboration d’un entrepôt de données (data warehouse) ;
    - la maîtrise et la protection des flux de données ;
    - l’élaboration de scénarios que l’entreprise pourrait rencontrer, afin de proposer des solutions d’anticipation ;
    - l’amélioration constante du système de récupération des données client, afin d’optimiser et d’agrandir le stock de données de l’entreprise.
    """)


with expander02:
    st.markdown("## Le métier de Data Engineer")
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
    - Maîtrise de divers systèmes d’exploitation : UNIX, Linux, Solaris...
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
    st. markdown("#### le DevOps appliqué à la data")
    st.write("Avec l'essor de l'apprentissage automatisé (Machine Learning ou ML) et de l'intelligence artificielle (IA), les données sont générées en masse. Collectées ensuite par les entreprises, elles ne sont pas toujours maîtrisées. La démarche DataOps vise à gérer ces données avec efficience. Des plateformes et des outils dédiés permettent de mettre en œuvre cette méthodologie. Les pratiques associées sont au cœur du métier de l'ingénieur DataOps.")
    st.markdown("### Le DataOps, qu'est-ce que c'est ?")
    st.markdown("""
        Le DataOps (Data Operations) optimise le cycle de vie des projets Data (relatifs aux données) et des analyses qui en sont issues. Selon le Gartner, il s’agit d’une pratique de gestion des données collaborative qui a pour but de favoriser l’exploitation de l’analytique dans les entreprises.
    """)
    st.markdown("### Quels sont les bénéfices du DataOps ?")
    st.markdown("""
        Le DataOps tend à accroître la rapidité et l’efficacité dans le traitement des données, afin qu’elles soient analysables et exploitables par les entreprises. Une meilleure productivité des équipes informatiques et une réduction des risques commerciaux constituent les principaux atouts de cette méthodologie.
    """)

    st.markdown("### Que recommande le DataOps Manifesto for agile ?")
    st.markdown("""
        Ce document référent en matière de méthodologie DataOps liste au total 18 principes. Ceux-ci comprennent notamment : la satisfaction continue du client, la valorisation des analyses de travail, l’acceptation du changement, la pluralité des rôles et des compétences dans les équipes (une diversité d’opinions encourageant l’innovation et la productivité), l’auto-organisation…

        Le manifeste reprend les principales caractéristiques de la méthode agile, appliquées plus spécifiquement à l’approche du DataOps.
    """)

    st.markdown("### Quels sont les principaux outils et plateformes de DataOps ?")
    st.markdown("""
        Des éditeurs proposent des outils et des plateformes qui supportent cette méthodologie afin de faciliter sa mise en œuvre au sein des équipes. Ces solutions ont pour principal objectif la gestion du cycle de vie d’un projet Data, de sa création à sa mise en production. Saagie, IBM et Datalytyx, par exemple, ont créé des solutions complètes pour intégrer ces pratiques.
    """)


    st.markdown("### DataOps ingénieur : quel profil de compétences, salaire et formation ?")
    st.markdown("""
        L’ingénieur DataOps doit avoir un bac + 5 en informatique orientée Big Data (cursus universitaire en plein développement), ou être titulaire d’un diplôme d’ingénieur spécialisé dans la Data. Il pilote le pipeline d’analyse de données en production, et vérifie la disponibilité et la performance des systèmes. Selon sa formation et son expérience, le salaire d’un ingénieur DataOps oscille entre 50 et 80 KE par an.
    """)

    st.markdown("### DataOps vs DevOps")
    st.markdown("""
        Le DataOps intègre la base de données dans les tests, il s’agit de DevOps appliqué aux données afin de répondre à un besoin plus précis. Les deux démarches sont collaboratives et impliquent plusieurs métiers, le DataOps étant spécifiquement orienté vers les entreprises tournées vers la Data.
    """)

    st.markdown("### DataOps vs MLOps")
    st.markdown("""
        D’un point de vue méthodologique, on retrouve les mêmes approches adaptées à des domaines différents, bien que liés. Le DataOps participe au déploiement, à l’analyse et au monitoring des données (Data), tandis que le MLOps est orienté vers la création, le déploiement et le monitoring des modèles d’apprentissage automatique (Machine Learning).
    """)


    