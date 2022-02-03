jq -c '.[]' build_job_ids.json | while read i; do
    echo "pull build $i"
done