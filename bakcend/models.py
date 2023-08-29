from app import db

class PDFFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"PDFFile(id={self.id}, filename={self.filename})"
