module Main where
 
import           Data.ByteString.Lazy.Char8   (pack)
import qualified Data.ByteString.Lazy         as B
 
header :: Int -> Int -> B.ByteString
header columns rows = pack $ unlines ["P6","800 400","255"]

remainder :: Int -> Int -> B.ByteString
remainder columns fileLength = pack $ replicate (fileLength `mod` columns) '\NUL'

main :: IO ()
main = do
  contents <- B.readFile "recording.wav"
  B.putStr $ header 800 400
  B.putStr contents
