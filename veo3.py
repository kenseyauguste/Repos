from google.cloud import aiplatform
from google.cloud.aiplatform.models import VideoModel

aiplatform.init(project="causal-lattice-460616-k8", location="us-central1")

video_model = VideoModel.from_pretrained("veo-3.0-generate-preview")
response = video_model.predict(
    prompt="A serene mountain lake at sunset with gentle ripples on the water",
    sample_count=1,
    video_duration="5s",
    aspect_ratio="16:9"
)

print(response)