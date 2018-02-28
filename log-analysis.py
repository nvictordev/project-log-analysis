import psycopg2

DBNAME = 'news'

def run_query(query):
	try:
		db = psycopg2.connect('dbname=' + DBNAME)
		c = db.cursor()
		c.execute(query)
		rows = c.fetchall()
		db.close()
		return rows
	except: 
		print ('Sorry, unable to connect to database')

def popular_three_articles():
	query = """
		SELECT articles.title, COUNT(*) AS views
		FROM articles, log
		WHERE log.path = CONCAT('/article/', articles.slug)
		GROUP BY articles.title ORDER BY views DESC LIMIT 3;"""
	popular_articles = run_query(query)
	print ('MOST POPULAR THREE ARTICLES OF ALL TIME')
	list_order = 1
	for i in popular_articles:
		print(str(list_order) + '.' + i[0] + ' - ' + str(i[1]) + ' views')
		list_order += 1
	print("")

def most_popular_authors():
	query = """
		SELECT authors.name, COUNT(*) AS views
		FROM authors, articles, log
		WHERE authors.id = articles.author AND log.path = CONCAT('/article/', articles.slug)
		GROUP BY authors.name
		ORDER BY views DESC;"""
	popular_authors = run_query(query)
	print ('MOST POPULAR ARTICLE AUTHORS OF ALL TIME')
	list_order = 1
	for i in popular_authors:
		print(str(list_order) + '.' + i[0] + ' - ' + str(i[1]) + ' views')
		list_order += 1
	print("")


if __name__ == '__main__':
	popular_three_articles()
	most_popular_authors()