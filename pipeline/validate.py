import duckdb

db_path = "ventes.duckdb"

con = duckdb.connect(db_path)

required_columns = {"date", "produit", "categorie", "quantite", "prix_unitaire", "ville "}

columns = con.execute("DESC ventes_rw").fetchall()

existing_columns = {raw_inf[0] for raw_inf in columns}

missing_columns = required_columns - existing_columns

if missing_columns:
	raise ValueError(f"Colones manquantes : {missing_columns}")

null_count = con.execute("""
	SELECT COUNT(*) FROM ventes_rw
	WHERE produit IS NULL OR quantite IS NULL OR prix_unitaire IS NULL
""").fetchone()[0]

con.close()

if null_count > 0:
	raise ValueError(f"Donnees invalides : {null_count} Lignes incompletes")

else:
	print("Validation reussie : schema et qualite minimale OK")


