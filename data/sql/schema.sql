CREATE TABLE "metrics" (
    "metric_id" INTEGER   NOT NULL,
    "product_id" INTEGER   NOT NULL,
    "product_name" VARCHAR(50)   NOT NULL,
    "date_time" TIMESTAMP   NOT NULL,
    "measured_weight" FLOAT   NOT NULL,
    "measured_height" FLOAT   NOT NULL,
    CONSTRAINT "pk_metrics" PRIMARY KEY (
        "metric_id"
     )
);

CREATE TABLE "products" (
    "product_id" INTEGER   NOT NULL,
    "product_name" VARCHAR(50)   NOT NULL,
    "weight_min" FLOAT   NOT NULL,
    "weight_max" FLOAT   NOT NULL,
    "height_min" FLOAT   NOT NULL,
    "height_max" FLOAT   NOT NULL,
    CONSTRAINT "pk_products" PRIMARY KEY (
        "product_id"
     )
);

ALTER TABLE "metrics" ADD CONSTRAINT "fk_metrics_product_id" FOREIGN KEY("product_id")
REFERENCES "products" ("product_id");

