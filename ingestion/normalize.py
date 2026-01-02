from core.database import SessionLocal
from core.models import (
    RawCoinPaprika,
    RawCoinGecko,
    NormalizedData,
)

def normalize():
    session = SessionLocal()

    # CoinPaprika → Normalized
    for r in session.query(RawCoinPaprika).all():
        exists = session.query(NormalizedData).filter_by(
            record_id=r.id,
            source="coinpaprika"
        ).first()
        if not exists:
            session.add(
                NormalizedData(
                    record_id=r.id,
                    name=r.name,
                    value=r.symbol,
                    source="coinpaprika"
                )
            )

    # CoinGecko → Normalized
    for r in session.query(RawCoinGecko).all():
        exists = session.query(NormalizedData).filter_by(
            record_id=r.id,
            source="coingecko"
        ).first()
        if not exists:
            session.add(
                NormalizedData(
                    record_id=r.id,
                    name=r.name,
                    value=r.symbol,
                    source="coingecko"
                )
            )

    session.commit()
    session.close()

if __name__ == "__main__":
    normalize()
