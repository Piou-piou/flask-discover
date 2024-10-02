from flask import Blueprint, Flask, jsonify
from database.DatabaseConnection import DatabaseConnection

# Création d'un blueprint pour les routes liées aux tâches
invoice_bp = Blueprint('invoice', __name__)

@invoice_bp.route('/invoices')
def index():
	db = DatabaseConnection()

	invoices = db.fetch_data('select * from crm_sales_invoice')

	return jsonify(invoices)
