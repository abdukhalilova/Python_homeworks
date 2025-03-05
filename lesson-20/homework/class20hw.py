import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")

# 1. Customer Purchases Analysis:
query = """
    SELECT c.CustomerId, c.FirstName || ' ' || c.LastName AS CustomerName, SUM(i.Total) AS TotalSpent
    FROM Customer c
    JOIN Invoice i ON c.CustomerId = i.CustomerId
    GROUP BY c.CustomerId
    ORDER BY TotalSpent DESC
    LIMIT 5;
"""
top_customers = pd.read_sql(query, conn)
print("Top 5 Customers with Highest Purchases:\n", top_customers)

# 2. Album vs. Individual Track Purchases:
album_query = """
    SELECT c.CustomerId,
           COUNT(DISTINCT il.InvoiceId) AS TotalInvoices,
           SUM(CASE WHEN il.TrackId IN (
               SELECT TrackId FROM Track
               WHERE AlbumId NOT IN (SELECT DISTINCT AlbumId FROM InvoiceLine)
           ) THEN 1 ELSE 0 END) AS IndividualTrackPurchases
    FROM Customer c
    JOIN Invoice i ON c.CustomerId = i.CustomerId
    JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId
    GROUP BY c.CustomerId;
"""
cust_purchases = pd.read_sql(album_query, conn)

cust_purchases['PrefersIndividualTracks'] = cust_purchases['IndividualTrackPurchases'] > 0
individual_track_percentage = cust_purchases['PrefersIndividualTracks'].mean() * 100
album_percentage = 100 - individual_track_percentage

print(f"Percentage of customers preferring individual tracks: {individual_track_percentage:.2f}%")
print(f"Percentage of customers preferring full albums: {album_percentage:.2f}%")

conn.close()
